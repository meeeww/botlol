import cv2
import numpy as np
import pyautogui as py
import pydirectinput
import math
import time
import random
import json

centroPantalla = (930, 500)

colorJugadorLower = np.array([24, 165, 198])
colorJugadorUpper = np.array([25, 225, 233]) # jugador
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

def kitear():
        moverDerecha = random.randint(40, 700)
        moverIzquierda = random.randint(100, 140)
        moverAltura = random.randint(50, 500)
        pydirectinput.moveTo(centroPantalla[0] + moverDerecha, centroPantalla[1] + moverAltura)
        pydirectinput.rightClick()
        wait(1)
        pydirectinput.moveTo(centroPantalla[0] - moverIzquierda, centroPantalla[1] + moverAltura)
        pydirectinput.rightClick()

def retroceder():
    moverIzquierda = random.randint(130, 200)
    moverAltura = random.randint(-100, 50)

    wait(0.1)

    pydirectinput.moveTo(centroPantalla[0] - moverIzquierda, centroPantalla[1] + moverAltura)
    pydirectinput.rightClick()

def comprar():
    pydirectinput.press('p')
    wait(0.5)
    pydirectinput.moveTo(811, 472)
    wait(0.1)
    pydirectinput.rightClick()
    wait(0.5)
    pydirectinput.press('p')

def irAMid():
    pydirectinput.moveTo(1761, 928)
    wait(0.1)
    pydirectinput.leftClick()
    pydirectinput.rightClick()
    wait(0.5)

def inGameController(campeonEscogido):
    print("# STARTING")

    global jugadorCoordenada
    global enemigosCoordenadas

    muerteCD = 0
    muerto = True
    atacar = []
    farmear = []
    hittearTorre = []
    enemigosCoordenadas = []
    minionsCoordenadas = []
    enemigosNumero = 0
    minionsNumero = 0
    minionsNumeroAliados = 0
    jugadorCoordenada = (1, 5)
    listaTorretas = []
    #Point(x=878, y=487) jugador en el centro
    py.screenshot().save("hey.png")
    img = cv2.imread("hey.png")

    #--------------------------------------------------------------conseguir jugador--------------------------------------------------------------
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, colorJugadorLower, colorJugadorUpper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 50:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
                jugadorCoordenada
                jugadorCoordenada = (x, y)
                muerto = False
    #--------------------------------------------------------------conseguir enemigos--------------------------------------------------------------
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, colorEnemigoLower, colorEnemigoUpper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 50:
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
        if distancia < (525*0.6):
            cv2.line(img, (primerPuntoX + 50, primerPuntoY + 100), (segundoPuntoX + 50, segundoPuntoY + 120), (0, 255, 0), 2)
            atacar.append([primerPuntoX + 100, primerPuntoY + 150, distancia])
            enemigosNumero = enemigosNumero + 1
        else:
            cv2.line(img, (primerPuntoX + 50, primerPuntoY + 100), (segundoPuntoX + 50, segundoPuntoY + 120), (0, 0, 255), 2)

    #--------------------------------------------------------------conseguir minions enemigos--------------------------------------------------------------
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, colorMinionLower, colorMinionUpper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 0:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
                minionsCoordenadas.append([x, y])

    for coordenada in minionsCoordenadas:
        primerPuntoX = coordenada[0]
        primerPuntoY = coordenada[1]
        segundoPuntoX = jugadorCoordenada[0]
        segundoPuntoY = jugadorCoordenada[1]

        distancia = math.sqrt(math.pow((segundoPuntoX-primerPuntoX), 2) + math.pow((segundoPuntoY-primerPuntoY), 2))
        #print(str(distancia) + " distancia")
        if distancia < (5000*0.6):
            mitad = math.floor(x + h)
            cv2.line(img, (primerPuntoX + 25, primerPuntoY + 40), (segundoPuntoX + 50, segundoPuntoY + 120), (0, 255, 255), 2)
            farmear.append([primerPuntoX + 25, primerPuntoY + 40, distancia])
            minionsNumero = minionsNumero + 1
        else:
            cv2.line(img, (primerPuntoX + 25, primerPuntoY + 40), (segundoPuntoX + 50, segundoPuntoY + 120), (0, 0, 255), 2)

    #--------------------------------------------------------------conseguir minions aliados--------------------------------------------------------------
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, colorMinionAliadoLower, colorMinionAliadoUpper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 0:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
                minionsNumeroAliados = minionsNumeroAliados + 1
                cv2.line(img, (x + 25, y + 40), (jugadorCoordenada[0] + 50, jugadorCoordenada[1] + 120), (255, 255, 255), 2)
    #--------------------------------------------------------------buscar a quien atacar enenemigos--------------------------------------------------------------
    maximo = 0
    aQuienAtacar = (0, 0)
    #print(atacar)

    for distanciaEnemigo in atacar:
        if(distanciaEnemigo[2] > maximo):
            maximo = distanciaEnemigo[2]
            aQuienAtacar = (distanciaEnemigo[0] - 15, distanciaEnemigo[1])
    #--------------------------------------------------------------HACE FALTA AÑADIR A QUIEN ATACAR MINIONS - y detectar torres - hecho--------------------------------------------------------------
    #print(farmear)
    #print("aqui")
    if aQuienAtacar == (0, 0):
        #print("-------")
        #print(atacar)
        #print(farmear)
        #print(hittearTorre)
        if atacar != []:
            aQuienAtacar = (atacar[0][0], atacar[0][1])
        elif farmear != []:
            aQuienAtacar = (farmear[0][0], farmear[0][1])
        elif hittearTorre != []:
            aQuienAtacar = (hittearTorre[0][0], hittearTorre[0][1])
    
    #print("------")
    #print(aQuienAtacar)
    #--------------------------------------------------------------BUSCAR TORRETAS--------------------------------------------------------------
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, colorTorretasMinimapLower, colorTorretasMinimapUpper)

    #conseguir en minimapa
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    midlane = [(1792, 896), (1804, 864), (1831, 843), (1842, 838)]
    torretasMid = [(1869, 816), (1860, 806)]
    nexo = (1877, 808)
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 1:
                x, y, w, h = cv2.boundingRect(contour)
                #cv2.rectangle(img, (x, y), (x + w, y + h), (252, 186, 3), 3)
                medioX = int((x + (x + w))/2)
                medioY = int((y + (y + h))/2)
                #print(medioX)
                cv2.circle(img, (medioX, medioY), 2, (252, 186, 3), 3)

                #print("-> " + str(x) + ", " + str(y))
                listaTorretas.append((x, y))# hay que chekear si le da click derecho a las torres - no da. buildeando
                #minionsNumeroAliados = minionsNumeroAliados + 1
                #cv2.line(img, (x + 25, y + 40), (jugadorCoordenada[0] + 50, jugadorCoordenada[1] + 120), (255, 255, 255), 2)

    #conseguir para atacar in-game
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, colorTorretasLower, colorTorretasUpper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 5:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (252, 186, 3), 3)
                medioX = int(w/2)
                medioY = int(h/2)
                #print(medioX)
                #cv2.circle(img, (medioX, medioY), 2, (20, 0, 255), 3)
                hittearTorre.append((x + 70, y + 175))# hay que chekear si le da click derecho a las torres - no da. buildeando
                #minionsNumeroAliados = minionsNumeroAliados + 1
                cv2.line(img, (x + medioX, y + medioY), (jugadorCoordenada[0] + 50, jugadorCoordenada[1] + 120), (255, 255, 255), 2)
    #print(listaTorretas)
    hayTorre = False
    nexoOpen = False
    siguienteTorre = (midlane[0][0], midlane[0][1])
    for torre in listaTorretas:
        if torre == (midlane[0][0], midlane[0][1]):
            hayTorre = True
            print("t1")

    if hayTorre == False:
        for torre in listaTorretas:
            if torre == (midlane[1][0], midlane[1][1]):
                hayTorre = True
                print("t2")
                siguienteTorre = (midlane[1][0], midlane[1][1])

    if hayTorre == False:
        for torre in listaTorretas:
            if torre == (midlane[2][0], midlane[2][1]):
                hayTorre = True
                print("t3")
                siguienteTorre = (midlane[2][0], midlane[2][1])

    if hayTorre == False:
        for torre in listaTorretas:
            if torre == (midlane[3][0], midlane[3][1]):
                hayTorre = True
                print("inhib")
                siguienteTorre = (midlane[3][0], midlane[3][1])

    if hayTorre == False:
        for torre in listaTorretas:
            if torre == (torretasMid[0][0], torretasMid[0][1]):
                hayTorre = True
                print("nextorre1")
                siguienteTorre = (torretasMid[0][0], torretasMid[0][1])

    if hayTorre == False:
        for torre in listaTorretas:
            if torre == (torretasMid[1][0], torretasMid[1][1]):
                hayTorre = True
                print("nextorre2")
                siguienteTorre = (torretasMid[1][0], torretasMid[1][1])

    if hayTorre == False:
        print("llegamos a nexo")
        for torre in listaTorretas:
            if torre == (nexo[0], nexo[1]):
                hayTorre = True
                nexoOpen = True
                print("nexoOpen")
                siguienteTorre = (nexo[0], nexo[1])

    #if hayTorre == True:
        #print("si hay, vamos a ")
        #print(siguienteTorre)
    
    print(aQuienAtacar)

    if aQuienAtacar == (0, 0):
        aQuienAtacar = siguienteTorre

    print(aQuienAtacar)
    
    #--------------------------------------------------------------detectar si muere--------------------------------------------------------------
    #print(muerto)
    #--------------------------------------------------------------CONTROLADOR hace falta detectar si muere--------------------------------------------------------------
    
    if muerto == True:#hay que detectar si muere
        comprar()
        wait(0.5)
    
    if muerto == False:
        if aQuienAtacar == (0, 0) and minionsNumeroAliados >= 1:
            print("hit torre")
            pydirectinput.moveTo(hittearTorre[0], hittearTorre[1])
            pydirectinput.rightClick()
            wait(0.5)
            #print("kitear")
            #kitear()
            #retroceder()
        elif aQuienAtacar == (0, 0) and minionsNumeroAliados == 0:
            #print("vamos a mid")
            irAMid()
            if config[campeonEscogido] == "mf":
                pydirectinput.press('w')
            wait(5)
        else:
            print("atacando minions o enemigos, numero habilidad: ")
            habilidad = random.randint(0, 10)
            print(habilidad)
            if habilidad == 10:
                pydirectinput.press('r')
                #if config[campeonEscogido]["r"]["esCancelable"] == True:
                    #wait(5)
            elif habilidad == 9:
                pydirectinput.press('e')
            elif habilidad == 8:
                pydirectinput.press('w')
            elif habilidad == 7:
                pydirectinput.press('q')

            pydirectinput.moveTo(aQuienAtacar[0], aQuienAtacar[1])
            pydirectinput.rightClick()
            #print("kitear")
            wait(2)
            #kitear()
    
    im = cv2.resize(img, (1000, 800))
    im2 = cv2.resize(mask, (1500, 1000))
    #cv2.imshow("webcam", im)
    #cv2.imshow("webcam2", im2)
    #cv2.waitKey()
    #print("hmm")
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('q')
    pydirectinput.press('r')
    pydirectinput.press('q')
    pydirectinput.press('w')
    pydirectinput.press('e')
    pydirectinput.keyUp('ctrl')
    pydirectinput.press('e')
    wait(0.1)
    #while enemigoDetectado == False:
    #atacarFuncion()