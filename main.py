import pyautogui
import time
import os
import colorama
from colorama import Fore
colorama.init(autoreset=True)


"""
1. python.exe -m pip install --upgrade pip
2. pip install Pillow --upgrade
3. pip install pyautogui
4. pip install colorama
5. pip install pytesseract
6. pip isntall tesseract

auto-py-to-exe -> para hacer deploy de .exe

"""
import os
os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
print(Fore.GREEN + " # STARTING BOT...")
# CREAR VARIABLES
location = None
chat_list = []
directory = os.listdir()
imageExplorador = "Explorador.PNG"

# CERRAR EXPLORADOR
while (location == None):
    try:
        location = pyautogui.locateOnScreen(imageExplorador)
    except Exception as e:
        print(e)

pyautogui.moveTo(location, duration=1)
pyautogui.click()
pyautogui.hotkey('alt', 'f4')
location = None
print(Fore.GREEN + " # CLOSED EXPLORER")
time.sleep(5)

"""
for file in directory:
    if file.startswith('Ch'):
        chat_list.append(file)

print("xf")

while (location == None):
    print("brooo")
    for image in chat_list:
        print("test")
        print(image)
        location = pyautogui.locateOnScreen(image)
        print(location)
        if (location != None):
            print("salimos")
            break

print("aqui2")

print(location)
pyautogui.moveTo(location, duration=1)
pyautogui.click()
location = None

while (location == None):
    try:
        location = pyautogui.locateOnScreen(imageChatBubble)
    except Exception as e:
        print(e)

print(location)
pyautogui.moveTo(location, duration=1)
pyautogui.click()
time.sleep(1)
pyautogui.write("Hola!!!")
pyautogui.press('enter')
location = None
"""