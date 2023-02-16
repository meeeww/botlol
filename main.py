import os
import cv2
import numpy as np
import math
import time
import json
import funciones as funciones
import time
import pyautogui as py
import pytesseract
import re
import colorama
from colorama import Fore
colorama.init(autoreset=True)


with open("config.json", "r") as jsonfile:
    config = json.load(jsonfile)
    print("Read successful")

usuario = config["username"]
contra = config["password"]

"""
1. python.exe -m pip install --upgrade pip
2. pip install Pillow --upgrade
3. pip install pyautogui
4. pip install colorama
5. pip install pytesseract
6. pip install tesseract

auto-py-to-exe -> para hacer deploy de .exe

"""

# CREAR VARIABLES
location = None
chat_list = []
directory = os.listdir()
imagenPass = "./imagenes/singin/contra.png"
imagenRiot = "./imagenes/singin/riot.png"
enCliente = False

# ABRIR LEAGUE
'''
print(Fore.GREEN + " # STARTING BOT...")
time.sleep(1)
funciones.iniciarLeague(imagenRiot, usuario, imagenPass, contra, enCliente, location)

# CONSEGUIR INFORMACION
time.sleep(30)
funciones.conseguirEsencias()

#IR A LOBBY
time.sleep(3)
funciones.crearLobby()
'''
#IN GAME
def wait(segundos):
  time.sleep(segundos)

def jugador():
  image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(image, colorJugadorLower, colorJugadorUpper)

  contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  if len(contours) != 0:
    for contour in contours:
      if cv2.contourArea(contour) > 300:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
        global jugadorCoordenada
        jugadorCoordenada = (x, y)



def kitear():
  wait(0.5)
  py.moveTo(centroPantalla[0] + 50, centroPantalla[1])
  py.mouseDown(button='right')
  py.mouseUp(button='right')
  wait(0.5)
  py.moveTo(centroPantalla[0] - 150, centroPantalla[1])
  py.mouseDown(button='right')
  py.mouseUp(button='right')
  cv2.waitKey()

colorJugadorLower = np.array([20, 150, 20])
colorJugadorUpper = np.array([25, 255, 255]) # jugador
colorEnemigoLower = np.array([2, 130, 20])
colorEnemigoUpper = np.array([5, 255, 255])# ENEMIGOS,

centroPantalla = (930, 500)




global jugadorCoordenada
global enemigosCoordenadas


enemigoDetectado = False

for x in range(5):
  atacar = []
  enemigosCoordenadas = []
  jugadorCoordenada = (1, 5)
  py.screenshot().save("hey.png")
  img = cv2.imread("hey.png")
  jugador()
  
  image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(image, colorEnemigoLower, colorEnemigoUpper)

  contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  if len(contours) != 0:
    for contour in contours:
      if cv2.contourArea(contour) > 500:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
        enemigosCoordenadas.append([x, y])
  
  for coordenada in enemigosCoordenadas:
      primerPuntoX = coordenada[0]
      primerPuntoY = coordenada[1]
      segundoPuntoX = jugadorCoordenada[0]
      segundoPuntoY = jugadorCoordenada[1]

      distancia = math.sqrt(math.pow((segundoPuntoX-primerPuntoX), 2) + math.pow((segundoPuntoY-primerPuntoY), 2))
      #print(str(distancia) + " distancia")
      if distancia < (550*0.6):
          cv2.line(img, (primerPuntoX + 50, primerPuntoY + 100), (segundoPuntoX + 50, segundoPuntoY + 120), (0, 255, 0), 2)
          atacar.append([primerPuntoX + 100, primerPuntoY + 150, distancia])
          enemigoDetectado = False
      else:
          cv2.line(img, (primerPuntoX + 50, primerPuntoY + 100), (segundoPuntoX + 50, segundoPuntoY + 120), (0, 0, 255), 2)

  #print(atacar)
  maximo = 0
  #aQuienAtacar = centroPantalla
  print(atacar)
  
  for distanciaEnemigo in atacar:
      if(distanciaEnemigo[2] > maximo): 
          maximo = distanciaEnemigo[2]
          aQuienAtacar = (distanciaEnemigo[0], distanciaEnemigo[1])
      

  #cv2.imshow("webcam", img)
  #cv2.waitKey()
  print("hmm")
  wait(0.5)
  #while enemigoDetectado == False:
  #atacarFuncion()
  print(aQuienAtacar)
  py.moveTo(aQuienAtacar)
  py.mouseDown(button='right')
  py.mouseUp(button='right')
  print("kitear")
  kitear()
  
      