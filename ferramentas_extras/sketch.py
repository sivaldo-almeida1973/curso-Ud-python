"""
Transformar imagens em sketchs (esboço)

#pip install numpy

import cv2 #pip install opencv-python

imagem = cv2.imread("imagem.jpg")

#criar e armazenar 
imagem_sketch = cv2.cvtColor('imagem', cv2.COLOR_BAYER_BG2BGR)
print(type(imagem_sketch))
print(imagem_sketch)
esboco = cv2.GaussianBlur(255-imagem_sketch,(31,31),0)
print(esboco)
print(type(esboco))

pincel = cv2.divide(imagem_sketch,255-esboco,scale=300.0)


cv2.imwrite('imagem.jpg')


-------------------------------------------------------

import cv2
import imutils


arquivo_reconhecimento = cv2.CascadeClassifier('cars.xml')

figura = cv2.imread('carros.jpg')
figura = imutils.resize(figura, width=min(400,figura.shape[1]))

dimensoes = arquivo_reconhecimento.detectMultiScale(figura)


for (x,y,w,h) in dimensoes:
  cv2.rectangle(figura,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow('Detecção', figura)
cv2.waitKey(0)
cv2.destroyAllWindows()






-------------------------------------------------



import cv2
import imutils


arquivo_reconhecimento = cv2.HOGDescriptor()

figura = cv2.imread('Facial.jpg')
figura = imutils.resize(figura, width=min(400,figura.shape[1]))

dimensoes = arquivo_reconhecimento.detectMultiScale(figura)
print(dimensoes)

for (x,y,w,h) in dimensoes:
  cv2.rectangle(figura,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow('Detecção', figura)
cv2.waitKey(0)
cv2.destroyAllWindows()

---------------------------------------------------------------

import cv2
import imutils


arquivo_reconhecimento = cv2.HOGDescriptor()
arquivo_reconhecimento.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

figura = cv2.imread('Pedestres.jpg')
figura = imutils.resize(figura, width=min(400,figura.shape[1]))

dimensoes = arquivo_reconhecimento.detectMultiScale(figura, winStride=(4,4), padding=(4,4), scale=1.05)
print(dimensoes)

for (x,y,w,h) in dimensoes:
  cv2.rectangle(figura,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow('Detecção', figura)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
#pip install numpy

#pip install numpy


