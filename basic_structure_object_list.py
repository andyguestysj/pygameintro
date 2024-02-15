# Import the built in code for pygame and pgzero
import pygame, pgzero, pgzrun

# WIDTH & HEIGHT are used by "go" to make the game window
WIDTH = 800
HEIGHT = 600

#### Alien Class
class Alien(Actor):
    def __init__(self, spriteImage,x,y,speed):
        ## let Actor class handle the creation of the sprite
        super().__init__(spriteImage,(x,y))
        self.speed = speed

    def update(self):
        self.x = self.x + self.speed
        if (self.x>WIDTH):
            self.x = -40
    
    def draw(self):
        super().draw()

def draw():
    # basic draw function. the (hidden) pygame zero game loop calls this function regularly
    # anything you want to draw to the screen should be drawn in here

    screen.fill((80,0,70))
    ### draw alien
    for object in alienList:
        object.draw()
    
def update():
    # basic update function. the (hidden) pygame zero game loop calls this function regularly
    # it should update every part of your game that needs to be updated
    # think of this function as a tick of the game clock
    
    for object in alienList:
        object.update()


######### Alien Object List###########
# For each object you create in your game you should initialise it, update it and draw it

alienList=[]
alienList.append(Alien('alien.png',370,550,10))
alienList.append(Alien('alien.png',370,250,12))
alienList.append(Alien('alien_hurt.png',100,400,5))




# start the code with pgzrun.go()
pgzrun.go()

# below is not what happens, it is a simplification to give an idea of the structure of the game
#def go():
#    makeGameWindow()   
#    gameRunning = True
#    while (gameRunning == True):
#       update()
#       draw()