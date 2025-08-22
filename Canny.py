#Bibliotecas
import cv2
#Nó se que hace esta linea
img = cv2.imread('cartas.jpg', 0)
bordeCanny = cv2.Canny(img, 100, 200)

cv2.imshow('Oringinal', img)
cv2.imshow('blur', bordeCanny)

cv2.waitKey(0)
cv2.destroyAllWindows()
