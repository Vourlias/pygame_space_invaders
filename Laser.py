# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:34:11 2017

@author: john
"""

#
# Laser class
#
import pygame
class Laser:
    def __init__(self, coord, color, size, speed, refline, voffset):
        self.x1 = coord[0]
        self.y1 = coord[1] + voffset
        self.size = size
        self.color = color
        self.speed = speed
        self.refline = refline

    def Show(self, surface , boolfirerate):
        if boolfirerate:
            self.color = (0,255,0)
            pygame.draw.line(surface, self.color, (self.x1, self.y1),(self.x1,self.y1-self.size),3)
        else:
            self.color = (255,0,0)
            pygame.draw.line(surface, self.color, (self.x1, self.y1),(self.x1,self.y1-self.size),3)


    def Move(self, time):
        distance = self.speed * time
        self.y1 += distance

    def DistanceTravelled(self):
        return abs(self.refline - self.y1)

    def GoneAbove(self,y):
        if self.y1<=y:
            return True
        else:
            return False

    def GoneBelow(self,y):
        if self.y1>=y:
            return True
        else:
            return False

    def GetXY(self):
        return (self.x1, self.y1)