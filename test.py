import pyautogui as py
import pytesseract
import time
import re

location = None
imageExplorador = "esencias.PNG"
while (location == None):
    try:
        location = py.locateOnScreen(imageExplorador)
    except Exception as e:
        print(e)

print(location)
location = None
print("lo tenemos")
#time.sleep(5)
img = py.screenshot(region=(1008, 180, 75, 26))
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\A8-PC00\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
esencias = pytesseract.image_to_string(img)
print("Tienes " + str(int(re.search(r'\d+', esencias).group())) + " esencias")