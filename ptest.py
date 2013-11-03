import pygame
import math
from pygame.locals import *
import pyganim
print(pygame.FULLSCREEN)
pygame.init()
windowSurface = pygame.display.set_mode((1600, 800),0 , 8)
BACKGROUNDCOLOR = (255,255,255)
windowSurface.fill(BACKGROUNDCOLOR)

def getSquirrelRect(sqpos):
   b = Rect(sqpos + 20, 730, 30,30)
   return b

def getPlayerRect(pos,ypos):
   b = Rect(pos, ypos, 30, 30)
   return b
  

def isNear(playerRect, otherRect):
	
	if playerRect.colliderect(otherRect):
		
		return True
	return False



# create the PygAnimation object
offsetx = 0
offsety = 0
manRight = pyganim.PygAnimation([('runningright.bmp',0.2),('runningright2.bmp', 0.2), ('runningright3.bmp', 0.2)])
manLeft = pyganim.PygAnimation([('runningleft.bmp',0.2),('runningleft2.bmp', 0.2), ('runningleft3.bmp', 0.2)])
animObj = pyganim.PygAnimation([('lookingatme.bmp', 0.2), ('walkingtowards.bmp', 0.2), ('walkingtowards2.bmp', 0.2)])
monleft = pyganim.PygAnimation([('monsterleft.bmp', 0.2)])
monright = pyganim.PygAnimation([('monsterright.bmp', 0.2)])
monup = pyganim.PygAnimation([('monsterup.bmp', 0.2)])
squirrel = pyganim.PygAnimation([('squirrel.bmp',0.2),('squirrel2.bmp',0.2),('squirrel3.bmp',0.2),('squirrel4.bmp',0.2),('squirrel5.bmp',0.2)])
squirrelb = pyganim.PygAnimation([('squirrelb.bmp',0.2),('squirrel2b.bmp',0.2),('squirrel3b.bmp',0.2),('squirrel4b.bmp',0.2),('squirrel5b.bmp',0.2)])
tree = pygame.image.load('tree.bmp')
treeRect = tree.get_rect()
monleft.play()
monright.play()
monup.play()
manLeft.play()
manRight.play()
squirrel.play()
squirrelb.play()
#house = pygame.image.load('house.bmp')
#houseRect = house.get_rect()
#farmer = pygame.image.load('farmer2.bmp')
#farmerRect = farmer.get_rect()
rock = pygame.image.load('rock.bmp')
rockRect = rock.get_rect()


	
standingstill = pyganim.PygAnimation([('lookingatme.bmp', 0.2)])
standingstill.play()
animObj.play()
#on.play()
monpos = 200
rate = 0
pos = 800
ypos = 400
moveup = False
movedown = False
moveLeft = False
moveRight = False
sqpos = 1400
rockposx = 1400
rockposy = 690
sq = squirrel
#squirrel is either atRock or atTree
atRock = True
while True: # main loop

    for event in pygame.event.get():
	if event.type == QUIT:
            pygame.quit()
            sys.exit()
	
	if event.type == KEYDOWN:
        	if event.key == ord('a'):
			moveLeft = True
                if event.key == ord('d'):
                        moveRight = True
                if event.key == ord('w'):
                        moveup = True
                if event.key == ord('s'):
                        movedown = True

	if event.type == KEYUP:
	        if event.key == ord('a'):
			pos = pos - 5
                    	moveLeft = False
                if event.key == ord('d'):
			pos = pos + 5
                        moveRight = False
                if event.key == ord('s'):
                        movedown = False
                        ypos = ypos + 5
                if event.key == ord('w'):
                        ypos = ypos - 5 
                        moveup = False
      
			
                    	
		if event.key == K_ESCAPE:
            		pygame.quit()
            		sys.exit()
    if moveLeft == True:
	pos = pos -1
    if moveRight == True:
        pos = pos +1
    if moveup == True:
        ypos = ypos -1
    if movedown == True:
        ypos = ypos +1


    windowSurface.fill(BACKGROUNDCOLOR)

    squirrelRect = getSquirrelRect(sqpos)


    sq.blit(windowSurface,(sqpos,730))

    treeRect.topleft = (400,400)

    windowSurface.blit(tree,treeRect) 
    
    rockRect.topleft = (rockposx,rockposy)
    windowSurface.blit(rock,rockRect)
    playerRect = getPlayerRect(pos,ypos)
    sqpos = sqpos + rate
   
    
    if isNear(playerRect,rockRect) and atRock and sqpos > 400:
       	sq = squirrel
    	rate = -4
    elif isNear(playerRect,treeRect) and not atRock and sqpos < 1400:
	sq = squirrelb
	rate = 4
    else:
	atRock = not atRock
        rate = 0
         
   

    

    if abs(monpos - pos) < 20:
	
	monup.blit(windowSurface,(monpos,300))
    elif pos > monpos:
	monright.blit(windowSurface,(monpos,300))
    elif pos < monpos:
	monleft.blit(windowSurface,(monpos,300))
    else:
	monup.blit(windowSurface,(monpos,300))
	

    if moveLeft == False and moveRight == False and moveup == False and movedown == False :
	standingstill.blit(windowSurface, (pos,ypos))
    else:
	if moveLeft == True:
		manLeft.blit(windowSurface,(pos,ypos))
	elif moveRight == True:
                manRight.blit(windowSurface,(pos,ypos))
	else:
	    	animObj.blit(windowSurface, (pos,ypos))
    #houseRect.topleft = (700,200)
    #windowSurface.blit(house,houseRect)
    #farmerRect.topleft = (700,500)
    #windowSurface.blit(farmer,farmerRect)
    pygame.display.update()