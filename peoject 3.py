import pygame
from pygame.locals import *
import sys, pygame
pygame.init()

import pygame
import time

pygame.init()

display_width = 1000
display_height = 600
z= 1000
c=600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

car_width = 20

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Star Trek')
clock = pygame.time.Clock()

carImg = pygame.image.load('ball.bmp')

Marimg = pygame.image.load('mars.jpeg')

def Mars(x,y):
    gameDisplay.blit(Marimg, (x-130, y-400))

def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('You Crashed')


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)
        car(x, y)
        Mars(z, c)



        if x > display_width - car_width or x < 0:
            crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

mars = (12, 23, 34)
pavo = (211, 23, 432)
user = (0, 0, 0)


def calcdistance(locA, locB):
    xdis = locA[0] - locB[0]
    ydis = locA[1] - locB[1]
    zdis = locA[2] - locB[2]

    totaldistance = (xdis ** 2 + ydis ** 2 + zdis ** 2) ** 0.5
    return totaldistance


def transfer():
    choice = input("mars is a transfer station, where else do you want to go")
    if choice == "pavo":
        print("The distance is", calcdistance(pavo, user))
    elif choice == "starting point":
        print("the distance is 42.76680956068619, welcome back")


def navigate():
    choice = input("where do you want to go")

    if choice == "mars":
        print("The distance is", calcdistance(mars, user))

        user == pavo

        transfer()




    elif choice == "pavo":
        print("The distance is", calcdistance(pavo, user), ",Pavo is the last station")
    elif choice != "mars" or "pavo":
        print("destination name isn't corret, please enter again.")
        navigate()


navigate()

