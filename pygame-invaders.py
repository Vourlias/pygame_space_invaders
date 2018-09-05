# Pygame Invaders
import pygame
import os

from Alien import Alien
from Craft import Craft
from Laser import Laser
from ScoreBoard_ShieldMeter import ScoreBoard
from ScoreBoard_ShieldMeter import ShieldMeter
from SpaceCraft import SpaceCraft
from SpaceBackGround_GameOverShow import SpaceBackground

from pygame.locals import *
from random import randint
from sys import exit

# Center Message on surface, used for blitting info text

def CenterMessage(screen, surface):
    return (screen.get_width() - surface.get_width())/2

# A function for the background music

def PlayMusic(soundfile):
    pygame.mixer.music.load(soundfile)
    pygame.mixer.music.play(-1)

# A function for the sound effects

def PrepareSound(filename):
    sound = pygame.mixer.Sound(filename)
    return sound
#
# Simple function to display message for Game Over
#

def GameOverShow(screen):
    font = pygame.font.SysFont("impact", 32)
    
    gameovertext = font.render("Game Over!",True,(255,255,255))
    text_x = CenterMessage(screen, gameovertext)
    screen.blit (gameovertext,(text_x,280))
    
    gameovertext = font.render("Press R to Restart", True, (255,255,255))
    text_x = CenterMessage(screen, gameovertext)
    screen.blit(gameovertext,(text_x,320))
    return



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def button(msg,screen,x,y,w,h,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        
        pygame.draw.rect(screen, ic,(x,y,w,h))
        
        font = pygame.font.SysFont("impact", 32)
        text = font.render(msg,True,ac)
        text_x = CenterMessage(screen,text)
        screen.blit(text,( x+30,y) )
        
        if click[0]  == 1 and action == "new_game":
                main()
        elif click[0] == 1 and action == "quit":
                pygame.quit()
                exit()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
        
        font = pygame.font.SysFont("impact", 32)
        text = font.render(msg,True,(255,255,255))
        text_x = CenterMessage(screen,text)
        screen.blit(text,( x+30,y ))



#Game Meny
def Game_intro():
    
    os.environ['SDL_VIDEO_CENTERED']='1'
    pygame.init()
    
    screenwidth,screenheight = (480,640)
    screen = pygame.display.set_mode((screenwidth,screenheight), DOUBLEBUF, 32)
    pygame.display.set_caption("Pygame Invaders")
    
    pygame.key.set_repeat(1,1)
    StarField = SpaceBackground(screenheight, "stars.png")
    
    game_intro = True
    
    while game_intro: 
        for event in pygame.event.get():
                if event.type == KEYDOWN:
                    key = pygame.key.get_pressed()
                    if key[K_q]:
                        pygame.quit()
                        exit()
                        
        StarField.Show(screen)
        
        font = pygame.font.SysFont("impact", 32)
        text = font.render("Space Invaders",True,(255,255,255))
        text_x = CenterMessage(screen, text)
        screen.blit (text,(text_x,150))

        
        button("New Game",screen,140,300,140,50,(0,0,0),(0,255,0),"new_game")
        button("Exit Game",screen,140,400,140,50,(0,0,0),(0,255,0),"quit")
        

        pygame.display.update()
        pygame.time.Clock()
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Main function, program entry point
#
def main():
    # Initialize pygame library and OS environment
	# The following will center the game window on the screen

    os.environ['SDL_VIDEO_CENTERED']='1'
    pygame.init()

    # Screen size and initial spaceship position

    screenwidth,screenheight = (480,640)
    spaceship_pos = (240, 540)

    # Initialize screen and set caption

    screen = pygame.display.set_mode((screenwidth,screenheight), DOUBLEBUF, 32)
    pygame.display.set_caption("Pygame Invaders")

    # Set keyboard repeat to super fast / delay to minimum

    pygame.key.set_repeat(1,1)

    # Prepare Sound Effects

    laser = PrepareSound("shoot.wav")
    explosion = PrepareSound("invaderkilled.wav")
    destroyed = PrepareSound("explosion.wav")

    # Initialize the background and spaceship objects

    spaceship_low = (0,0)
    spaceship_high = (screenwidth, screenheight)
    StarField = SpaceBackground(screenheight, "stars.png")
    shipimages = ('spaceship2.png', 'spaceship3.png')
    SpaceShip = SpaceCraft(shipimages,spaceship_pos, spaceship_low, spaceship_high,laser)

    # Initialize fire lists (ours and aliens)

    firelist=[]
    alienfirelist = []

    # Set the background scrolling speed

    backspeed = 100

    # Initialize some objects and game variables

    score = ScoreBoard(0,0,"impact",32)
    shield = ShieldMeter(200,10,250,75)
    laserdownlimit = screenheight - 40
    GameOver = False


    # Start the background music

    PlayMusic("spaceinvaders.ogg")

    # Images used for the aliens

    alienimage=('alien1.png','alien2.png','alien3.png','alien4.png','alien5.png')

    # Number of aliens per 'wave'

    numofaliens = 8
    AlienShips = []

    # Initialize the clock object and set framerate

    clock = pygame.time.Clock()
    framerate = 60

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #arxika tick
    powerup_Duration_Start_Fire_Rate = 0
    powerup_Duration_Start_X2_Score = 0
    powerup_Duration_Start_Immune = 0
    
    #metavlites gia na kserw ean einai energopoihmeno ena powerup
    boolx2 = False
    boolimmune = False
    boolfirerate = False    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    
    
    # imageindex & flashcount used for alternating between normal
    # and 'hit' images

    imageindex = 0
    flashcount = 0

    while True:
        time = clock.tick(framerate)/1000.0
        

        if not AlienShips:
            # AlienShips empty means we need to create new 'wave'
            AlienShips = [ Alien(alienimage[randint(0,len(alienimage)-1)],
                                            [randint(20,screenwidth-80),
                                             randint(20,screenheight-140)],
                                             randint(100,150),
                                             randint(100,150)) for i in range(0,numofaliens) ]

        # shipspeed is zeroed at every cycle of the loop
        shipspeed_x = 0
        shipspeed_y = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == USEREVENT + 1:
                if flashcount < 10:
                    flashcount += 1
                    if imageindex == 1:
                        imageindex = 0
                    else:
                        imageindex = 1
                else:
                    imageindex = 0
                    flashcount = 0
                    pygame.time.set_timer(USEREVENT+1,0)
            if event.type == KEYDOWN:
                # This returns a list of True/False where the index is the
                # code of the key pressed. Fortunately pygame.locals provides
                # symbolics for these codes
                key = pygame.key.get_pressed()
                if key[K_q]:
                    pygame.quit()
                    exit()
                if key[K_r] and GameOver:
                    GameOver = False
                    shield.SetValue(250)
                    score.SetValue(0)
                if key[K_LEFT]:
                    shipspeed_x = -300
                if key[K_RIGHT]:
                    shipspeed_x = 300
                if key[K_UP]:
                    shipspeed_y = -300
                if key[K_DOWN]:
                    shipspeed_y = 300
                if key[K_SPACE] and not GameOver:
                    if firelist:
                        # Only fire if last shot has travelled
        					   # a minimum distance
                        if powerup_Duration_Start_Fire_Rate + 5 < (pygame.time.get_ticks()/1000):
                            if firelist[-1].DistanceTravelled() >=  150:
                                firelist.append(SpaceShip.Fire())
                                boolfirerate = False
                        else:
                            if firelist[-1].DistanceTravelled() >=  50:
                                firelist.append(SpaceShip.Fire())
                                boolfirerate = True
                            
                    else:
                        # or if there is no shot
                        firelist.append(SpaceShip.Fire())


        # Move the SpaceShip by the specified amount

        SpaceShip.Move(shipspeed_x, shipspeed_y, time)

        # Show all the objects, background first (or it will erase everything else!)
        StarField.Scroll(backspeed, time)
        StarField.Show(screen)
        SpaceShip.Show(screen,imageindex)

        # Show and move the aliens

        for AlienShip in AlienShips:
            AlienShip.Show(screen)
            AlienShip.Move(time)
            if randint(0,10)==9:
                if alienfirelist:
                    if alienfirelist[-1].DistanceTravelled()>=100:
                        alienfirelist.append(AlienShip.Fire())
                else:
                    alienfirelist.append(AlienShip.Fire())

        for theshot in firelist:
            theshot.Move(time)
            theshot.Show(screen,boolfirerate)
            if theshot.GoneAbove(0):
                firelist.remove(theshot)
            else:
                for AlienShip in AlienShips:
                    if AlienShip.rect.collidepoint(theshot.GetXY()):
        
                        if powerup_Duration_Start_X2_Score + 5 > (pygame.time.get_ticks()/1000):
                            score.Change(20)
                        else:
                            boolx2 = False
                            score.Change(10)
                            
                        explosion.play()
                        if score.GetValue() % 100 == 0:
                            shield.Increase(25)
                        if theshot in firelist:
                            firelist.remove(theshot)
                        AlienShips.remove(AlienShip)
                        
                        #kanw ena roll gia na dw ean tha tyxei kapio powerup
                        roll = randint(0,60)
                        if roll >=8 and roll <10:
                            #firerate
                            powerup_Duration_Start_Fire_Rate = (pygame.time.get_ticks())/1000
                            boolfirerate = True                        
                            
                        elif roll >=6 and roll <8:
                            #x2 score
                            powerup_Duration_Start_X2_Score = (pygame.time.get_ticks())/1000
                            boolx2 = True                                  
                            
                        elif roll >= 4 and roll <6:
                            #immune for y seconds
                            powerup_Duration_Start_Immune = (pygame.time.get_ticks())/1000
                            boolimmune = True
                            
                        
                        
             
        #elegxos laser ean efige apo ta oria tis othonis kai ean mas xtypise
        for theshot in alienfirelist:
            theshot.Move(time)
            theshot.Show(screen,boolimmune)
            if theshot.GoneBelow(laserdownlimit):
               alienfirelist.remove(theshot)
            else:
               if SpaceShip.rect.collidepoint(theshot.GetXY()) and not GameOver:
                 
                   if powerup_Duration_Start_Immune + 5 < (pygame.time.get_ticks()/1000):
                       destroyed.play()
                       pygame.time.set_timer(USEREVENT+1,25)
                       shield.Decrease(25)
                       boolimmune = False
                   
                   if theshot in alienfirelist:
                       alienfirelist.remove(theshot)

        
        score.Show(screen,boolx2)
        shield.Show(screen,boolimmune)
        if shield.GetValue() <= 0:
          GameOverShow(screen)
          GameOver = True

        pygame.display.update()

# End main loop

# Start program
Game_intro()
main()
