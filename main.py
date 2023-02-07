import pyautogui
import time
import os

"""
1. python.exe -m pip install --upgrade pip
2. pip install Pillow --upgrade
3. pip install pyautogui

"""

location = None
imageFile = 'VisualStudio.PNG'
chat_list = []
directory = os.listdir()
imageChat = "Chat.PNG"
imageChatSecond = "Chat2.PNG"
imageChatBubble = "Omar.PNG"


for file in directory:
    if file.startswith('Chat'):
        chat_list.append(file)

while (location == None):
    try:
        location = pyautogui.locateOnScreen(imageFile)
    except Exception as e:
        print(e)

print(location)
pyautogui.moveTo(location, duration=1)
pyautogui.click()
pyautogui.click()
location = None


while (location == None):
    for image in chat_list:
        print(image)
        location = pyautogui.locateOnScreen(image)
        if(location != None):
            print("salimos")
            break


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