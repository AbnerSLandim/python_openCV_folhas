import cv2
import numpy as np
import os
import csv

pasta = "imagens"

resultados = []

for arquivo in sorted(os.listdir(pasta)):

    caminho = os.path.join(pasta, arquivo)
    img = cv2.imread(caminho)

    if img is None:
        continue

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)

    green_pixels = np.sum(mask > 0)
    total_pixels = img.shape[0] * img.shape[1]

    ratio = green_pixels / total_pixels

    if ratio > 0.4:
        categoria = "saudavel"
    else:
        categoria = "doente"

    resultados.append([arquivo, categoria, ratio])

print(resultados)

with open("resultado.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["imagem", "categoria", "confianca"])

    for r in resultados:
        writer.writerow(r)