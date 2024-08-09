import cv2
import numpy as np

# Carrega a imagem
image = cv2.imread('./img/CNI.png')

# Converte para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplica uma limiarização
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Encontra os contornos
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Especifique a dimensão conhecida do objeto de referência em cm
known_width_cm = 2.0  # exemplo: 2 cm

# Encontre o contorno do objeto de referência (assumindo que seja o maior contorno)
reference_contour = max(contours, key=cv2.contourArea)

# Calcula a largura do objeto de referência em pixels
_, _, ref_width_px, _ = cv2.boundingRect(reference_contour)

# Calcula a razão pixels-para-cm
pixels_per_cm = ref_width_px / known_width_cm

# Medir o maior contorno que não seja o de referência
object_contour = sorted(contours, key=cv2.contourArea, reverse=True)[1]

# Calcula o retângulo delimitador do contorno do objeto
x, y, obj_width_px, obj_height_px = cv2.boundingRect(object_contour)

# Converte as medidas de pixels para cm
obj_width_cm = obj_width_px / pixels_per_cm
obj_height_cm = obj_height_px / pixels_per_cm

# Exibe o tamanho do objeto em cm
print(f"Largura do objeto: {obj_width_cm:.2f} cm, Altura do objeto: {obj_height_cm:.2f} cm")

# Desenha o retângulo ao redor do objeto e do objeto de referência
cv2.rectangle(image, (x, y), (x + obj_width_px, y + obj_height_px), (0, 255, 0), 2)
cv2.rectangle(image, cv2.boundingRect(reference_contour), (255, 0, 0), 2)

# Exibe a imagem com os retângulos desenhados
cv2.imshow('Imagem com Contornos', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
