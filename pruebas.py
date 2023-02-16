import cv2
import numpy as np
import time

image = cv2.imread('hey.png', cv2.IMREAD_COLOR)

def jugador(image):
    
    enemigo = cv2.imread('imagenes/ingame/jugadorprueba2.png', cv2.IMREAD_COLOR)

    h, w = enemigo.shape[:2]

    method = cv2.TM_CCOEFF_NORMED

    threshold = 0.90

    start_time = time.time()

    res = cv2.matchTemplate(image, enemigo, method)

    # fake out max_val for first run through loop
    max_val = 1
    while max_val > threshold:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_val > threshold:
            res[max_loc[1]-h//2:max_loc[1]+h//2+1, max_loc[0]-w//2:max_loc[0]+w//2+1] = 0
            image = cv2.rectangle(image,(max_loc[0],max_loc[1]), (max_loc[0]+w+1, max_loc[1]+h+163), (0,255,0) )
            print("x: " + str(max_loc[0]) + "," + str(max_loc[1]))
            print("y: " + str(max_loc[0]+w+1) + "," + str(max_loc[1]+h+163))

            x1 = max_loc[0]
            y1 = max_loc[1]

            x2 = max_loc[0]+w+1
            y2 = max_loc[1]+h+163

            x = x1+x2/2
            y = y1+y2/2
            print(x)
            print(y)
            #image = cv2.line(image, (int(x)), int(y), (0,255,0), 1)

def enemigo(image):
    
    enemigo = cv2.imread('imagenes/ingame/enemigo.png', cv2.IMREAD_COLOR)

    h, w = enemigo.shape[:2]

    method = cv2.TM_CCOEFF_NORMED

    threshold = 0.60

    start_time = time.time()

    res = cv2.matchTemplate(image, enemigo, method)

    # fake out max_val for first run through loop
    max_val = 1
    mean = enemigo.mean()
    print("el mean es " + str(mean))
    while max_val > threshold:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print(str(max_val))
        if max_val > threshold:
            res[max_loc[1]-h//2:max_loc[1]+h//2+1, max_loc[0]-w//2:max_loc[0]+w//2+1] = 0
            image = cv2.rectangle(image,(max_loc[0],max_loc[1]), (max_loc[0]+w+1, max_loc[1]+h+163), (0,255,0) )
            print("x: " + str(max_loc[0]) + "," + str(max_loc[1]))
            print("y: " + str(max_loc[0]+w+1) + "," + str(max_loc[1]+h+163))

            x1 = max_loc[0]
            y1 = max_loc[1]

            x2 = max_loc[0]+w+1
            y2 = max_loc[1]+h+163

            x = x1+x2/2
            y = y1+y2/2
            print(x)
            print(y)
            #image = cv2.line(image, (int(x)), int(y), (0,255,0), 1)
            
jugador(image)
enemigo(image)
cv2.imwrite('output.png', image)
cv2.imshow('output.png', image)
cv2.waitKey()