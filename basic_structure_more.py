# Import the built in code for pygame and pgzero
import pygame, pgzero, pgzrun

# WIDTH & HEIGHT are used by "go" to make the game window
WIDTH = 800
HEIGHT = 600

######### Alien Object ###########
# For each object you create in your game you should initialise it, update it and draw it
### Initialise Alien
alien = Actor('alien.png')
alien.x = 370
alien.y = 550

### updateAlien
def updateAlien():
    alien.x = alien.x + 10
    if (alien.x>800):
        alien.x = -40

def draw():
    # basic draw function. the (hidden) pygame zero game loop calls this function regularly
    # anything you want to draw to the screen should be drawn in here

    # screen.fill((80,0,70))
    ### draw alien
    alien.draw()
    
def update():
    # basic update function. the (hidden) pygame zero game loop calls this function regularly
    # it should update every part of your game that needs to be updated
    # think of this function as a tick of the game clock
    
    updateAlien()




# start the code with pgzrun.go()
pgzrun.go()

# below is not what happens, it is a simplification to give an idea of the structure of the game
#def go():
#    makeGameWindow()   
#    gameRunning = True
#    while (gameRunning == True):
#       update()
#       draw()