import time
import os
import pyautogui as py
import pytesseract
import re
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def iniciarLeague(imagenRiot, usuario, imagenPass, contra, enCliente, location):
    os.startfile('C:\Riot Games\League of Legends\LeagueClient.exe')
    print(Fore.GREEN + " # OPENING LEAGUE")
    while(enCliente == False):
        print(Fore.GREEN + " # WAITING 1 MINUTE FOR LEAGUE TO START UP CORRECTLY")
        while (location == None):
            time.sleep(3)
            try:
                enCliente = True
                print(Fore.RED + " # LAUNCHER NOT OPENED")
                location = location = py.locateOnScreen(imagenRiot)
            except Exception as e:
                print(e)

    print(Fore.GREEN + " # SIGNING IN")
    py.write(usuario)
    location = None

    while (location == None):
        try:
            location = py.locateOnScreen(imagenPass)
        except Exception as e:
            print(e)

    py.moveTo(location)
    py.click()
    py.write(contra)
    location = None
    time.sleep(1)
    print(Fore.GREEN + " # SIGNED IN")
    py.press("enter")
    print(Fore.GREEN + " # OPENING CLIENT")

def conseguirEsencias():
    location = None
    imageExplorador = "./imagenes/lobby/esencias.PNG"
    while (location == None):
        try:
            location = py.locateOnScreen(imageExplorador, grayscale=True, confidence=0.8)
        except Exception as e:
            print(e)

    #time.sleep(5)
    img = py.screenshot("test.png", region=(location.left, location.top, 100, 26))
    py.screenshot(region=(location.left, location.top, 75, 26))
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\srjza\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    esencias = pytesseract.image_to_string(img)
    esencias = str(int(re.search(r'\d+', esencias).group()))
    print(Fore.BLUE + " # BE: " + esencias)

def crearLobby():
    print("hola")