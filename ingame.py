import cv2
import numpy as np
import pyautogui as py
import pydirectinput
import math
import time
import random
import json

centroPantalla = (930, 500)

colorJugadorLower = np.array([22, 170, 195])
colorJugadorUpper = np.array([26, 225, 230]) # jugador
colorEnemigoLower = np.array([3, 144, 153])
colorEnemigoUpper = np.array([3, 210, 206])# ENEMIGOS,
colorMinionLower = np.array([0, 130, 195])
colorMinionUpper = np.array([1, 145, 209])# MINIONS,
colorMinionAliadoLower = np.array([103, 160, 195])
colorMinionAliadoUpper = np.array([104, 161, 210])# MINIONS ALIADOS,
colorTorretasMinimapLower = np.array([0, 180, 150])#torretas
colorTorretasMinimapUpper = np.array([1, 190, 200])#torretas
colorTorretasLower = np.array([2, 200, 42])#torretas
colorTorretasUpper = np.array([2, 200, 172])#torretas

with open("./src/campeones.json", "r") as jsonfile:
    config = json.load(jsonfile)

def wait(segundos):
        time.sleep(segundos)

def comprar():
    pydirectinput.press('p')
    wait(0.5)
    pydirectinput.moveTo(811, 472)
    wait(0.1)
    pydirectinput.rightClick()
    wait(0.5)
    pydirectinput.press('p')

def clickDerecho():
    pydirectinput.rightClick()
    pydirectinput.mouseUp(button='right')

def clickIzquierdo():
    pydirectinput.leftClick()
    pydirectinput.mouseUp(button='left')

def irAMid():
    pydirectinput.moveTo(1797, 956)
    wait(0.1)
    clickIzquierdo()
    clickDerecho()
    wait(0.5)

def conseguirJugador(jugadorCoordenada, img):
    muerto = True
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, colorJugadorLower, colorJugadorUpper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0: #checkear jugador
        for contour in contours:
            if cv2.contourArea(contour) > 50:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1) #hacemos un rectangulo para ver si detecta la vida
                jugadorCoordenada = (x + 50, y + 100) #se añade x + 50, y + 100 para calcular el centro del modelo
                muerto = False

    if jugadorCoordenada != (0, 0): #revisar si se encontro jugador
        muerto = False

    return jugadorCoordenada, muerto

def conseguirEnemigo(enemigosCoordenadas, img):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, colorEnemigoLower, colorEnemigoUpper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 50:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)#hacemos un rectangulo para ver si detecta la vida
                enemigosCoordenadas.append((x + 50, y + 100))#se añade x + 50, y + 100 para calcular el centro del modelo

    #if enemigosCoordenadas != (0, 0):
        

def inGameController(campeonEscogido):
    print("# STARTING")

    jugadorCoordenada = (0, 0)
    enemigosCoordenadas = []


    muerteCD = 0
    muerto = True
    atacar = []
    farmear = []
    hittearTorre = []
    
    minionsCoordenadas = []
    enemigosNumero = 0
    minionsNumero = 0
    minionsNumeroAliados = 0
    
    listaTorretas = []
    #Point(x=878, y=487) jugador en el centro
    #py.screenshot().save("hey2.png")
    img = cv2.imread("hey2.png")

    #--------------------------------------------------------------conseguir jugador--------------------------------------------------------------
    jugadorCoordenada, muerto = conseguirJugador(jugadorCoordenada, img)
    #--------------------------------------------------------------conseguir enemigos--------------------------------------------------------------
    conseguirEnemigo(enemigosCoordenadas, img)
    #--------------------------------------------------------------conseguir distancias--------------------------------------------------------------
    print(jugadorCoordenada)
    print(muerto) #hace falta calcular que enemigo esta más cerca para atacarle
    for enemigo in enemigosCoordenadas:
        cv2.line(img, jugadorCoordenada, enemigo, (255, 0, 0), 2)

    cv2.imshow("webcam2", img)
    cv2.waitKey()