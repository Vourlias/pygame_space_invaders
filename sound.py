# Sound effects
import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
laser = pygame.mixer.Sound("./sounds/laser.wav")
laser.play()
while pygame.mixer.get_busy():
	clock.tick()
