import cv2
import numpy as np
import pyautogui as py
import math
import time

def wait(segundos):
    time.sleep(segundos)

colorJugadorLower = np.array([22, 150, 20])
colorJugadorUpper = np.array([25, 255, 255]) # jugador
colorEnemigoLower = np.array([2, 130, 20])
colorEnemigoUpper = np.array([5, 255, 255])# ENEMIGOS,

centroPantalla = (960, 540)

img = cv2.imread("hey.png")
global enemigosCoordenadas
enemigosCoordenadas = []
global jugadorCoordenada
jugadorCoordenada = (1, 5)

def jugador():
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, colorJugadorLower, colorJugadorUpper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
                global jugadorCoordenada
                jugadorCoordenada = (x, y)


def enemigo():
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, colorEnemigoLower, colorEnemigoUpper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
                global enemigosCoordenadas
                enemigosCoordenadas.append([x, y])

def atacarFuncion():
    py.moveTo(aQuienAtacar)
    py.rightClick()

def kitear():
    py.moveTo(centroPantalla[0] + 50, centroPantalla[1])
    py.rightClick()
    wait(0.5)
    py.moveTo(centroPantalla[0] - 50, centroPantalla[1])
    py.rightClick()

jugador()
enemigo()
atacar = []
enemigoDetectado = False
print(enemigosCoordenadas)

for coordenada in enemigosCoordenadas:
    primerPuntoX = coordenada[0]
    primerPuntoY = coordenada[1]
    segundoPuntoX = jugadorCoordenada[0]
    segundoPuntoY = jugadorCoordenada[1]

    distancia = math.sqrt(math.pow((segundoPuntoX-primerPuntoX), 2) + math.pow((segundoPuntoY-primerPuntoY), 2))
    print(str(distancia) + " distancia")
    if distancia < (550*0.6):
        cv2.line(img, (primerPuntoX + 50, primerPuntoY + 100), (segundoPuntoX + 50, segundoPuntoY + 120), (0, 255, 0), 2)
        atacar.append([primerPuntoX + 50, primerPuntoY + 150, distancia])
        enemigoDetectado = True
    else:
        cv2.line(img, (primerPuntoX + 50, primerPuntoY + 100), (segundoPuntoX + 50, segundoPuntoY + 120), (0, 0, 255), 2)

print(atacar)
maximo = 0
for distanciaEnemigo in atacar:
    if(distanciaEnemigo[2] > maximo):
        maximo = distanciaEnemigo[2]
        aQuienAtacar = (distanciaEnemigo[0], distanciaEnemigo[1])

cv2.imshow("webcam", img)
cv2.waitKey()

wait(0.5)
while enemigoDetectado == False:
    atacarFuncion()
    kitear()

