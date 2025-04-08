import os
import sys
import pygame
from pygame.locals import * # type: ignore
import random

BASE = os.path.dirname(__file__)

if 'PSMOVEAPI_LIBRARY_PATH' not in os.environ:
    os.environ['PSMOVEAPI_LIBRARY_PATH'] = os.path.join(BASE, 'build')

sys.path.insert(0, os.path.join(BASE, 'bindings', 'python'))

import psmoveapi

pygame.init()

class Move(psmoveapi.PSMoveAPI):
    def __init__(self):
        super().__init__()
        self.quit = False

    def on_connect(self, controller):
        print(type(controller))
        print('Controle Conectado: ', controller)

    def on_update(self, controller: psmoveapi.Controller):
        global coresN, corPsMove, corAtual
        acc = controller.accelerometer
        # print(acc)

        if -0.5 < acc.x < 0.5 and 0.7 < acc.y < 1.1: # type: ignore
            corPsMove = 'vermelho'
            self.changeColor(controller, coresN[corPsMove])

        elif 0.8 < acc.x < 1.1 and -0.3 < acc.y < 0.3: # type: ignore
            corPsMove = 'amarelo'
            self.changeColor(controller, coresN[corPsMove])

        elif -1.1 < acc.x < -0.8 and -0.3 < acc.y < 0.3: # type: ignore
            corPsMove = 'azul'
            self.changeColor(controller, coresN[corPsMove])

        elif -0.5 < acc.x < 0.5 and -1.1 < acc.y < -0.7: # type: ignore
            corPsMove = 'verde'
            self.changeColor(controller, coresN[corPsMove])
        
        if controller.now_pressed(psmoveapi.Button.MOVE):
            coresIguais(corPsMove, corAtual)

    def changeColor(self, controller: psmoveapi.Controller, color: tuple):
        controller.color = psmoveapi.RGB(color[0], color[1], color[2])        

    def on_disconnect(self, controller):
        print('Controller disconnected:', controller)

def coresIguais(cor1, cor2):
    global pontuacao, corAtual
    if cor1 == cor2:
        pontuacao += 1
        corAtual = random.choice(['vermelho','amarelo','verde','azul'])

tela = pygame.display.set_mode((640,480),0)
pygame.display.set_caption("colmeia")


cores = {
    'vermelho': (255,0,0),
    'amarelo': (255,255,0),
    'verde': (0,255,0),
    'azul': (0,0,255)
}

coresN = {
    'vermelho': (1,0,0),
    'amarelo': (1,1,0),
    'verde': (0,1,0),
    'azul': (0,0,1)
}
desenhaCor = pygame.draw.rect(tela, cores['vermelho'],(0,0,50,50))
corAtual = 'vermelho'
corPsMove = 'vermelho'
pontuacao = 0
correctColor = False
running = True

move = Move()
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    if pygame.key.get_pressed()[K_UP]:
        corAtual = random.choice(['vermelho','amarelo','verde','azul'])
    move.update()

    desenhaCor = pygame.draw.rect(tela, cores[corAtual],(0,0,640,480))
    pygame.display.flip()
