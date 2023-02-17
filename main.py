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
#PICKEAR


#IN GAME
ingame.inGameController()