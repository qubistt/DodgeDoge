# 1 - importing required modules
import pygame
from pygame.locals import *

# 2 - initialise pygame
pygame.init()
width, height = (640, 480)
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerposition=[100,100]

# 3 - Load images
player = pygame.image.load("assets/images/player.png")
grass = pygame.image.load("assets/images/grass.png")
castle = pygame.image.load("assets/images/castle.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    for x in range(width//grass.get_width()+1):
        for y in range(height//grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345 ))
    # 6 - draw the screen elements
    screen.blit(player, playerposition)
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        if keys[pygame.K_UP]:
            keys[0]=True
        elif keys[pygame.K_LEFT]:
            keys[1]=True
        elif keys[pygame.K_DOWN]:
            keys[2]=True
        elif keys[pygame.K_RIGHT]:
            keys[3]=True
        
        # 9 - Move player
        if keys[0]:
            playerposition[1] -= 5
        elif keys[2]:
            playerposition[1] += 5
        if keys[1]:
            playerposition[0] -= 5
        elif keys[3]:
            playerposition[0] += 5
