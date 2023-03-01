import os
import cv2
import numpy as np
import math
import time
import json
import funciones as funciones
import ingame as ingame
import time
import pyautogui as py
import pytesseract
import re
import colorama
from colorama import Fore
colorama.init(autoreset=True)


with open("./src/config.json", "r") as jsonfile:
    config = json.load(jsonfile)
    print("Read successful")

usuario = config["username"]
contra = config["password"]

"""
python.exe -m pip install --upgrade pip
pip install Pillow --upgrade
pip install pyautogui
pip install colorama
pip install pytesseractq
pip install tesseract
pip install numpy
pip install opencv-python
pip install PyDirectInput

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
#PICKEAR

campeonEscogido = "mf"
#IN GAME
time.sleep(2)
print(py.position())
#ingame.comprar()
#ingame.irAMid()
#time.sleep(30)
for x in range(3):
    ingame.inGameController(campeonEscogido)