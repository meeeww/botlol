import pyautogui

"""
1. python.exe -m pip install --upgrade pip
2. pip install Pillow --upgrade
3. pip install pyautogui

"""

location = None
imageFile = 'Captura.PNG'

while (location == None):
    try:
        location = pyautogui.locateOnScreen(imageFile)
    except Exception as e:
        print(e)

print(location)