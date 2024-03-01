"""importamos libreria"""

import cv2
import requests
import time

print("Bienvenido...")
time.sleep(2)
print("Transformemos una imagen a boceto...")
time.sleep(2)
print("Tu primer paso es introducir la url de la imagen a transformar...")
time.sleep(2)

# Proceso para descargar la imagen
# link de la imagen
url_img = input("Introduce la URL de la imagen por favor... ")


# nombre con el que se guardara la img
name_img = input("¿Que nombre deseas ponerle a la imagen? ")

# Obetenemos la imagen con requetst
img = requests.get(url_img, timeout=10).content

with open(name_img, 'wb') as handler:
    handler.write(img)

time.sleep(2)
print("La imagen se ha descargado...")
time.sleep(2)

# proceso para transformar la imagen descargada a boceto

print("Leyendo arhivo...")
time.sleep(2)

img_to_change = cv2.imread(name_img)  # leemos imagen descargada
cv2.imshow("Image", img_to_change)
cv2.waitKey(0)
time.sleep(1)

print("Transformando imagen...")
time.sleep(2)


# transformamos a escala de grises
img_to_gray_scale = cv2.cvtColor(img_to_change, cv2.COLOR_BGR2GRAY)
cv2.imshow("New Img", img_to_gray_scale)
cv2.waitKey(0)

print("Escala de grises...")
time.sleep(2)

inverted_image = 255 - img_to_gray_scale  # Invertimos escala de grises
cv2.imshow("Inverted", inverted_image)
cv2.waitKey()

print("Invirtiendo colores...")
time.sleep(2)


# aplicamos funcion gausiana
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

print("Funion gausiana...")
time.sleep(2)


inverted_blurred = 255 - blurred  # invertimos funcion gausiana
pencil_sketch = cv2.divide(img_to_gray_scale, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)

print("Imagen tranformada...")  # mensaje de finalización
time.sleep(1)
print("gracias...")
