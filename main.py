#Gülhan Polat 02205076071
import cv2
import numpy as np

goruntu = cv2.imread('sokak.jpeg')
cv2.imshow('goruntu1', goruntu)
#işlenicek resim 
foto = cv2.imread('sokak.jpeg',0)
cv2.imshow('goruntu1-0', foto)

[h, w] = foto.shape
goruntu = np.zeros([h, w], dtype=np.uint8)
for i in range(h):
    for j in range(w):
        goruntu[i, j] = 255 - foto[i, j]

cv2.imshow("Ters resim", goruntu)
cv2.waitKey()