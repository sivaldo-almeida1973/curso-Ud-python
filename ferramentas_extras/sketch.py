"""
Transformar imagens em sketchs (esboço)
"""
#pip install numpy

import cv2 #pip install opencv-python

imagem = cv2.imread("imagem.jpg")

#criar e armazenar 
imagem_sketch = cv2.cvtColor(imagem, cv2.COLOR_BAYER_BG2BGR)
print(type(imagem_sketch))
print(imagem_sketch)
esboco = cv2.GaussianBlur(255-imagem_sketch,(31,31),0)
print(esboco)
print(type(esboco))