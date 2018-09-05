# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:33:27 2017

@author: john
"""
import pygame
from Craft import Craft
from Laser import Laser

class Alien(Craft):
    def __init__(self, imagefile, coord, speed_x, speed_y):
        imagefiles = (imagefile,)
        super(Alien, self).__init__(imagefiles, coord)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.shot_height = 10
        self.firebaseline = self.ship_height
        self.firecolor=(255,255,0)
        self.firespeed = 200
    def Move(self, time):
        super(Alien,self).Move(self.speed_x, self.speed_y,time)
        if self.rect[0] >= 440 or self.rect[0] <= 10:
            self.speed_x = -self.speed_x
        if self.rect[1] <= 10 or self.rect[1] >= 440:
            self.speed_y = -self.speed_y
    def Fire(self):
        theshot = Laser((self.rect[0]+self.ship_midwidth, self.rect[1]+self.firebaseline),
                        self.firecolor, self.shot_height, self.firespeed,self.rect[1]+self.firebaseline, 0)
        return theshot
    def Show(self, surface):
        imageindex = 0
        super(Alien,self).Show(surface,imageindex)