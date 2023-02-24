import cv2

# Carga la imagen
img = cv2.imread("colores.jpg")

# Redimensiona la imagen a un tamaño de ancho 
width = 300
height = int(img.shape[0] * (width / img.shape[1]))
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# Guarda la imagen redimensionada
cv2.imwrite("resized_image.jpg", resized)
