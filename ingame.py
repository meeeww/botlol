import cv2 as cv
import numpy as np
from PIL import ImageGrab
import pyautogui as py

while True:
    py.screenshot().save("hey.png")
    screen = cv.imread('hey.png', cv.IMREAD_ANYCOLOR)

    jugador = cv.imread('imagenes/ingame/jugador.png', cv.IMREAD_ANYCOLOR)
    enemigo = cv.imread('imagenes/ingame/enemigo.png', cv.IMREAD_ANYCOLOR)

    resultJugador = cv.matchTemplate(screen, jugador, cv.TM_CCOEFF_NORMED)
    resultEnemigo = cv.matchTemplate(screen, enemigo, cv.TM_CCOEFF_NORMED)

    min_valJugador, max_valJugador, min_locJugador, max_locJugador = cv.minMaxLoc(resultJugador)
    min_valEnemigo, max_valEnemigo, min_locEnemigo, max_locEnemigo = cv.minMaxLoc(resultEnemigo)


    print("best match: " + str(min_valJugador))
    print("second best: " + str(max_valJugador))
    print("second 3: " + str(min_locJugador))
    print("second 4: " + str(max_locJugador))
    print("best match" + str(max_valJugador))
    

    encontrado = False

    threshold = 0.8
    if max_valJugador >= threshold:
        print("found")

        needle_w = jugador.shape[1]
        needle_h = jugador.shape[0]

        top_left = max_locJugador
        bottom_right = ((top_left[0]) + needle_w, top_left[1] + needle_h + 163)

        cv.rectangle(screen, top_left, bottom_right,
                            color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
        print(bottom_right[1] + 100)
        
        #cv.imshow("Result", screen)
        #cv.waitKey()
        encontrado = True
    else:
        print("holi")

    if max_valEnemigo >= threshold:
        print("found")

        needle_w = enemigo.shape[1]
        needle_h = enemigo.shape[0]

        top_left = max_locEnemigo
        bottom_right = ((top_left[0]) + needle_w, top_left[1] + needle_h + 163)

        cv.rectangle(screen, top_left, bottom_right,
                            color=(0, 0, 255), thickness=2, lineType=cv.LINE_4)
        print(bottom_right[1] + 100)
        
        
        encontrado = True
    else:
        print("holi")



    if encontrado == True:
        cv.imshow("Result", screen)
        cv.waitKey()
#restar rectangulo 1 - rectangulo 2 para conseguir la distancia

#(737, 241, 163, 241)
#box = cv.selectROI("selecionar", screen, fromCenter=False)
#box = (737, 241, 163, 241)


