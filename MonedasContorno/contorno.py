import cv2

def mostrarImagen(name, src, x, y):
    cv2.imshow(name,src)
    cv2.moveWindow(name, x, y)

#Leemos imagen
imagen = cv2.imread('MonedasContorno\piezas.jpg')
#Redimensionamos imagen
imagen_redimensionada = cv2.resize(imagen,(400,400))
mostrarImagen('image_redimnensionada',imagen_redimensionada, 900, 50)
#Pasamos a grises
grises =  cv2.cvtColor(imagen_redimensionada, cv2.COLOR_BGR2GRAY)
mostrarImagen('imagen en gris',grises, 1350, 50)
#buscamos umbral
_ , umbral =cv2.threshold(grises, 100, 255, cv2.THRESH_BINARY)
mostrarImagen('imagen umbral',umbral, 900, 500)
#Buscamos contorno
contorno, jerarquia = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#Dibujamos contornos
imagen_contorno = imagen_redimensionada
cv2.drawContours(imagen_contorno, contorno, -1, (12, 249, 36), 3)
mostrarImagen('imagen con contorno',imagen_contorno, 1350, 500)


cv2.waitKey(0)
cv2.destroyAllWindows()


