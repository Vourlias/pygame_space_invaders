# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:33:48 2017

@author: john
"""

# The class for our ship
import pygame
from Craft import Craft
class SpaceCraft(Craft):
    def __init__ (self, imagefile, coord, min_coord, max_coord,lasersound):
        super(SpaceCraft,self).__init__(imagefile,coord)
        self.min_coord = min_coord
        self.max_coord = (max_coord[0]-self.ship_width, max_coord[1]-self.ship_height)
        self.lasersound = lasersound

    def Move(self, speed_x, speed_y, time):
        super(SpaceCraft,self).Move(speed_x, speed_y, time)
        for i in (0,1):
            if self.rect[i] < self.min_coord[i]:
                self.rect[i] = self.min_coord[i]
            if self.rect[i] > self.max_coord[i]:
                self.rect[i] = self.max_coord[i]

    def Fire(self):
        self.lasersound.play()
        return super(SpaceCraft,self).Fire()