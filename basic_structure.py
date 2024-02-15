# Import the built in code for pygame and pgzero
import pygame, pgzero, pgzrun



def draw():
    # basic draw function. the (hidden) pygame zero game loop calls this function regularly
    # anything you want to draw to the screen should be drawn in here
    pass

def update():
    # basic update function. the (hidden) pygame zero game loop calls this function regularly
    # it should update every part of your game that needs to be updated
    # think of this function as a tick of the game clock
    pass






# start the code with pgzrun.go()
pgzrun.go()

# below is not what happens, it is a simplification to give an idea of the structure of the game
#def go():
#    makeGameWindow()
#    gameRunning = True
#    while (gameRunning == True):
#       update()
#       draw()