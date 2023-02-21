import cv2
import numpy as np
import pyautogui as py
import math
import time

centroPantalla = (930, 500)

def wait(segundos):
        time.sleep(segundos)

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

def inGameController():
    colorJugadorLower = np.array([23, 150, 180])
    colorJugadorUpper = np.array([25, 225, 255]) # jugador
    colorEnemigoLower = np.array([3, 144, 153])
    colorEnemigoUpper = np.array([3, 210, 206])# ENEMIGOS,
    colorMinionLower = np.array([0, 130, 100])
    colorMinionUpper = np.array([1, 145, 255])# MINIONS,
    colorMinionAliadoLower = np.array([103, 160, 195])
    colorMinionAliadoUpper = np.array([104, 161, 210])# MINIONS ALIADOS,
    colorTorretasPlacasLower = np.array([0, 0, 0])#torretas
    colorTorretasPlacasUpper = np.array([10, 255, 255])#torretas
    colorTorretasLower = np.array([0, 180, 150])#torretas
    colorTorretasUpper = np.array([1, 190, 200])#torretas

    global jugadorCoordenada
    global enemigosCoordenadas


    atacar = []
    farmear = []
    enemigosCoordenadas = []
    minionsCoordenadas = []
    enemigosNumero = 0
    minionsNumero = 0
    minionsNumeroAliados = 0
    jugadorCoordenada = (1, 5)
    listaTorretas = []
    #py.screenshot().save("hey.png")
    img = cv2.imread("hey.png")

    #--------------------------------------------------------------conseguir jugador--------------------------------------------------------------
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, colorJugadorLower, colorJugadorUpper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 300:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
                jugadorCoordenada
                jugadorCoordenada = (x, y)
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
        if distancia < (525*0.6):
            mitad = math.floor(x + h)
            cv2.line(img, (primerPuntoX + 25, primerPuntoY + 40), (segundoPuntoX + 50, segundoPuntoY + 120), (0, 255, 255), 2)
            farmear.append([primerPuntoX + 100, primerPuntoY + 150, distancia])
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
    print(atacar)

    for distanciaEnemigo in atacar:
        if(distanciaEnemigo[2] > maximo):
            maximo = distanciaEnemigo[2]
            aQuienAtacar = (distanciaEnemigo[0], distanciaEnemigo[1])
    #--------------------------------------------------------------HACE FALTA AÑADIR A QUIEN ATACAR MINIONS--------------------------------------------------------------
    print(minionsNumeroAliados)
    if aQuienAtacar == (0, 0):
        aQuienAtacar = (atacar[0][0], atacar[0][1])
    #--------------------------------------------------------------BUSCAR TORRETAS--------------------------------------------------------------
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, colorTorretasLower, colorTorretasUpper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    botlane = [(1894, 996), (1883, 938), (1888, 904), (1890, 895)]
    midlane = [(1819, 938), (1829, 909), (1850, 892), (1860, 890)]
    toplane = [(1748, 853), (1801, 859), (1840, 855), (1854, 859)]
    torretasMid = [(1881, 871), (1872, 864)]
    nexo = (1886, 861)
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 0:
                x, y, w, h = cv2.boundingRect(contour)
                #cv2.rectangle(img, (x, y), (x + w, y + h), (252, 186, 3), 3)
                medioX = int((x + (x + w))/2)
                medioY = int((y + (y + h))/2)
                print(medioX)
                cv2.circle(img, (medioX, medioY), 2, (252, 186, 3), 3)
                listaTorretas.append((x, y))# hay que chekear si le da click derecho a las torres
                #minionsNumeroAliados = minionsNumeroAliados + 1
                #cv2.line(img, (x + 25, y + 40), (jugadorCoordenada[0] + 50, jugadorCoordenada[1] + 120), (255, 255, 255), 2)

    print(listaTorretas)
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

    if hayTorre == True:
        print("si hay, vamos a ")
        print(siguienteTorre)
    #--------------------------------------------------------------FINAL--------------------------------------------------------------
    print(aQuienAtacar)
    im = cv2.resize(img, (960, 540))
    im2 = cv2.resize(mask, (960, 540))
    cv2.imshow("webcam", im)
    #cv2.imshow("webcam2", im2)
    cv2.waitKey()
    print("hmm")
    wait(0.5)
    #while enemigoDetectado == False:
    #atacarFuncion()
    print(aQuienAtacar)
    '''
    py.moveTo(aQuienAtacar)
    py.mouseDown(button='right')
    py.mouseUp(button='right')
    print("kitear")
    kitear()
    '''