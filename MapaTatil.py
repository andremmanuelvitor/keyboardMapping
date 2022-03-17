import KeyPressModule
import PressionamentoTecla as pt
import numpy as np
from time import sleep
import cv2
import math

###### PARAMETROS ######
fSpeed = 150 / 10  # Velocidade Frontal em cm/s (15cm/s)
aSpeed = 360 / 10  # Velocidade Angular em Graus/s (36°/s)
intervalo = 0.25  # ntervalo de tempo
dDeslocamento = fSpeed * intervalo  # Deslocamento em cm
aDeslocamento = aSpeed * intervalo  # Deslocamento em graus
########################

x, y = 500, 500
a = 0
yaw = 0
pt.init()

# Como o objetivo final é usar esse módulo para controlar o drone Tello, os comandos abaixo ficarão comentados.
# Uma vez que estou apenas brincando com a possibilidade de controlar as coordenadas cartesianas com o teclado.

#me = tello.Tello()

#me.connect()

#print(me.get_battery())

pontos = [(0, 0), (0, 0)]  # lista vazia para armazenar os pontos


def getTecladoInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    velocidade = 15
    avelocidade = 50
    global x, y, a, yaw
    d = 0

    if pt.getKey("RIGHT"):
        lr = velocidade
        d = -dDeslocamento
        a = 180

    elif pt.getKey("LEFT"):
        lr = -velocidade
        d = dDeslocamento
        a = -180

    if pt.getKey("UP"):
        fb = velocidade
        d = dDeslocamento
        a = 270

    elif pt.getKey("DOWN"):
        fb = -velocidade
        d = -dDeslocamento
        a = -90

    if pt.getKey("w"):
        ud = velocidade

    elif pt.getKey("s"):
        ud = -velocidade

    if pt.getKey("a"):
        yv = -avelocidade
        yaw -= aDeslocamento

    elif pt.getKey("d"):
        yv = avelocidade
        yaw += aDeslocamento

    # if kp.getKey("q"): me.land(); sleep(3)
    # if kp.getKey("e"): me.takeoff()

    sleep(intervalo)
    a += yaw
    x += int(d * math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))

    return [lr, fb, ud, yv, x, y]  # retornar em uma lista fica mais facil para acessar os dados futuramente


def desenharPontos(img, pontos):
    for ponto in pontos:
        cv2.circle(img, ponto, 5, (255, 0, 0), cv2.FILLED)

    cv2.circle(img, pontos[-1], 10, (0, 255, 0), cv2.FILLED)

    cv2.putText(img, f'({(pontos[-1][0]-500)/100}), {(pontos[-1][1]-500)/100})m',
                (pontos[-1][0]+10, pontos[-1][1]+30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1)

while True:

    vals = getTecladoInput()

    #Comando comentado pelo mesmo motivo acima
    # me.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = np.zeros((1000, 1000, 3), np.uint8) # usando a biblioteca numpy para "interpretar" como matriz

    if pontos[-1][0] != vals[4] or pontos[-1][1] != vals[5]:
        pontos.append((vals[4], vals[5]))

    desenharPontos(img, pontos)
    cv2.imshow("Mapa", img)
    cv2.waitKey(1) #delay de 1 ms