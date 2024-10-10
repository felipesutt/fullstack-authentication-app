from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
import json

import os
import cv2

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
    if request.method == 'GET':
        return JsonResponse({'access_level': user_access_level})
    
@csrf_exempt
def get_information(request):
    global user_access_level
    if request.method == 'GET':
        accessible_properties = EnvironmentalData.objects.filter(required_access_level__lte=user_access_level)
        properties_list = list(accessible_properties.values('id', 'propriedade', 'responsavel', 'content', 'required_access_level'))
        return JsonResponse({'propriedades': properties_list})
    return JsonResponse({'message':'Erro'})