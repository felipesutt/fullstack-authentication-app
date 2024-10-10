import os
import cv2
from time import sleep

fingerprint_img = cv2.imread("fingerprint_detection/3__M_Left_index_finger.BMP") # Lendo a imagem principal
fingerprint_img = cv2.resize(fingerprint_img, None,fx=2.5, fy=2.5) # Resize da image

sift_algorithm = cv2.SIFT.create() # Criação do objeto do algoritmo SIFT(Scale Invariant Feature Transform)
kp1, descriptor_1 = sift_algorithm.detectAndCompute(fingerprint_img, None) # Rodar o algoritmo SIFT na imagem principal, kp1 é uma tupla de objetos KEYPOINT do opencv, descriptor é um array

files_path = os.listdir("fingerprint_detection/SOCOFing/Real") # Path de cada imagem a ser comparada

for file in files_path[3000:3400]: # Iterar cada imagem, cortei a lista pra ser mais rapido
    print(file) # Printar a pasta que ele esta acessando no momento

    to_compare_fingerprint = cv2.imread("fingerprint_detection/SOCOFing/Real/" + file)
    
    kp2, descriptor_2 = sift_algorithm.detectAndCompute(to_compare_fingerprint, None) # Rodar o algoritmo SIFT na imagem a comparar

    matches = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10},
                                    {}).knnMatch(descriptor_1, descriptor_2, k=2) # Retorna uma tupla de objetos Dmatch do opencv, NÃO SEI COMO FUNCIONA DIREITO
    
    match_points = []
    for p, q in matches: # Encontrar pontos correspondentes, NÃO SEI COMO FUNCIONA DIREITO TAMBÉM
        if p.distance < 0.1 * q.distance:
            match_points.append(p)

    keypoints = 0 # NAO SEI OQ FAZ AQUI E PARA QUE SERVE
    if len(kp1) < len(kp2):
        keypoints = len(kp1)
    else:
        keypoints = len(kp2)

    best_score = 0
    print(len(match_points) / keypoints, len(match_points) ,keypoints)
    if len(match_points) / keypoints * 100 > best_score: # Calcular o melhor score e guardar o nome da imagem que bateu
        print("ENTROU AQUI")
        best_score = len(match_points) / keypoints * 100
        filename = file
        image = to_compare_fingerprint

print("BEST MATCH: " + filename)
print("SCORE: " + str(best_score))

result = cv2.drawMatches(fingerprint_img, kp1, image, kp2, match_points, None)
# result = cv2.resize(result, None,fx=4, fy=4)

cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()