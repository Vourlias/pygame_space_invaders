# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:32:30 2017

@author: john
"""

# The superclass for both our ship and the aliens
import pygame
from Laser import Laser

class Craft(object):
    def __init__ (self, imagefiles, coord):
        self.shape = [(pygame.transform.scale((pygame.image.load(imagefile)),(50,50))) for imagefile in imagefiles]
        
        self.ship_width = self.shape[0].get_width()
        self.ship_height = self.shape[0].get_height()
        self.rect = pygame.Rect(coord,(self.ship_width, self.ship_height))
        self.ship_midwidth = self.ship_width / 2
        self.firecolor=(255,0,0)
        self.firespeed = -800
        self.shotlength = 20

    def Show(self, surface,imageindex):
        surface.blit(self.shape[imageindex],(self.rect[0],self.rect[1]))

    def Move(self,speed_x,speed_y, time):
        distance_x = speed_x * time
        distance_y = speed_y * time
        self.rect.move_ip(distance_x,distance_y)

    def Fire(self):
        shot = Laser((self.rect[0]+self.ship_midwidth, self.rect[1]),
                     self.firecolor,self.shotlength,self.firespeed,self.rect[1],15)
        return shot
