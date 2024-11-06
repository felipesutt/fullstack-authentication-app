from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
import json

import os
import cv2
import numpy as np
from datetime import datetime
import base64

from .models import EnvironmentalData

global user_access_level

def index(request):
    return JsonResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def login_user(request):
    global user_access_level
    if request.method == 'POST':
        data = json.loads(request.body)
        user = authenticate(request, username=data.get('usernameField'), password=data.get('passwordField'))
        if user is not None:
            user_access_level = user.access_level
            return JsonResponse({'access_level': user_access_level})
        else:
            return JsonResponse({'message':'User dont have login'})

@csrf_exempt
def digital_authentication(request):
    global user_access_level
    if request.method == 'POST':
        data = json.loads(request.body)

        if data.get('type') == 'correct':
            fingerprint_img = cv2.imread("server/authentication/fingerprint_detection/3__M_Left_index_finger.BMP")  # Lendo a imagem principal correta
        elif data.get('type') == 'wrong':
            fingerprint_img = cv2.imread("server/authentication/fingerprint_detection/11__M_Right_ring_finger.BMP") # Lendo a imagem principal errada

        fingerprint_img = cv2.resize(fingerprint_img, None, fx=2.5, fy=2.5)  # Resize da imagem

        sift_algorithm = cv2.SIFT.create()  # Criação do objeto do algoritmo SIFT(Scale Invariant Feature Transform)
        kp1, descriptor_1 = sift_algorithm.detectAndCompute(fingerprint_img, None)  # Rodar o algoritmo SIFT na imagem principal, kp1 é uma tupla de objetos KEYPOINT do opencv, descriptor é um array

        files_path = os.listdir("server/authentication/fingerprint_detection/SOCOFing/Real")  # Path de cada imagem a ser comparada

        best_score = 0  # Inicializar o melhor score
        best_filename = None  # Inicializar o nome do melhor arquivo
        best_image = None  # Inicializar a melhor imagem
        best_kp2 = None  # Inicializar os keypoints da melhor imagem
        best_match_points = None  # Inicializar os pontos de correspondência

        for file in files_path: # Iterar cada imagem, cortei a lista pra ser mais rapido
            print(file)  # Printar o nome do arquivo que está sendo acessado

            to_compare_fingerprint = cv2.imread("server/authentication/fingerprint_detection/SOCOFing/Real/" + file)
            to_compare_fingerprint = cv2.resize(to_compare_fingerprint, None, fx=2.5, fy=2.5)  # Resize da imagem

            kp2, descriptor_2 = sift_algorithm.detectAndCompute(to_compare_fingerprint, None)  # Rodar o algoritmo SIFT na imagem a comparar

            # Comparar descritores usando Flann Matcher
            matches = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10}, {}).knnMatch(descriptor_1, descriptor_2, k=2) # Retorna uma tupla de objetos Dmatch do opencv, NÃO SEI COMO FUNCIONA DIREITO

            match_points = []
            for p, q in matches: # Encontrar pontos correspondentes, NÃO SEI COMO FUNCIONA DIREITO TAMBÉM
                if p.distance < 0.1 * q.distance:
                    match_points.append(p)

            # Calcular a quantidade de keypoints
            keypoints = min(len(kp1), len(kp2))

            # Calcular o score
            score = len(match_points) / keypoints * 100 if keypoints > 0 else 0

            print(f"Score: {score:.2f}, Matches: {len(match_points)}, Keypoints: {keypoints}")

            # Atualizar se o score atual for melhor
            if score > best_score:
                print("Melhor correspondência encontrada!")
                best_score = score
                best_filename = file
                best_image = to_compare_fingerprint
                best_kp2 = kp2
                best_match_points = match_points

        # Exibir o resultado da melhor correspondência
        if best_image is not None:
            print("BEST MATCH: " + best_filename)
            print("SCORE: " + str(best_score))
        else:
            print("Nenhuma correspondência encontrada.")

        return JsonResponse({'access_level': user_access_level, 'score': best_score})
    
@csrf_exempt
def facial_authentication(request):
    global user_access_level
    if request.method == 'POST':
        data = json.loads(request.body)
        
        image_data = data.get('image') # Pega a imagem do objeto
        image_data = image_data.replace('data:image/jpeg;base64,', '') # Renomeia a string da imagem base64

        image_bytes = base64.b64decode(image_data) # Decodifica a imagem base64
        np_image = np.frombuffer(image_bytes, np.uint8) # Converte os bytes da imagem em um array numpy
        image = cv2.imdecode(np_image, cv2.IMREAD_COLOR) # Decodifica a imagem usando openCV

        file_name = 'imagem.jpg'
        file_path = os.path.join('server/authentication/facial_detection',file_name)
        cv2.imwrite(file_path, image)

        # Configuração dos detectores Haar Cascade
        detectorFace = cv2.CascadeClassifier('server/authentication/facial_detection/cascade/haarcascade_frontalface_default.xml')
        detectorOlho = cv2.CascadeClassifier('server/authentication/facial_detection/cascade/haarcascade-eye.xml')

        # Instanciando LBPH Face Recognizer
        reconhecedor = cv2.face.LBPHFaceRecognizer_create()
        reconhecedor.read("server/authentication/facial_detection/classifier/classificadorLBPH.yml")

        height, width = 220, 220  # Tamanho definido para redimensionar a imagem
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL

        # Converte o frame para escala de cinza
        imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Deteção da face no frame
        faceDetect = detectorFace.detectMultiScale(
            imageGray,
            scaleFactor=1.5,
            minSize=(35, 35),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Loop para processar cada face detectada
        for (x, y, h, w) in faceDetect:
            # Extrai e redimensiona a face detectada
            face_img = cv2.resize(imageGray[y:y + h, x:x + w], (width, height))

            # Realiza o reconhecimento facial
            id, confianca = reconhecedor.predict(face_img)  # ID do rosto e confiança

            print('a',id, confianca)

            # Verificação do ID e criação da resposta
            if id == 1:
                name = "Usuário"
                return JsonResponse({'access_granted': False, 'user': name, 'confidence': confianca})
            elif id == 2:
                name = "Diretor"
                return JsonResponse({'access_granted': False, 'user': name, 'confidence': confianca})
            elif id == 3 and confianca <= 50:
                name = "Ministro"
                return JsonResponse({'access_granted': True, 'user': name, 'confidence': confianca})
            else:
                return JsonResponse({'access_granted': False, 'user': 'Desconhecido', 'confidence': confianca})

        # Caso nenhuma face seja detectada
        return JsonResponse({'access_granted': False, 'user': 'Nenhuma face detectada', 'confidence': None})
    
@csrf_exempt
def get_information(request):
    global user_access_level
    if request.method == 'GET':
        accessible_properties = EnvironmentalData.objects.filter(required_access_level__lte=user_access_level)
        properties_list = list(accessible_properties.values('id', 'propriedade', 'responsavel', 'content', 'required_access_level'))
        return JsonResponse({'propriedades': properties_list})
    return JsonResponse({'message':'Erro'})