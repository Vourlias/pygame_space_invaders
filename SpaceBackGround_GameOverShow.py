# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:37:41 2017

@author: john
"""

# This is the class for the scrolling background
import pygame
import pygame.locals

class SpaceBackground:
    def __init__(self, screenheight, imagefile):
        self.shape = pygame.transform.scale((pygame.image.load(imagefile)),(480,640))
        self.coord = [0,0]
        self.coord2 = [0, -screenheight]
        self.y_original = self.coord[1]
        self.y2_original = self.coord2[1]

    def Show(self, surface):
        surface.blit(self.shape, self.coord)
        surface.blit(self.shape, self.coord2)

    def Scroll(self, speed_y, time):
        distance_y = speed_y * time
        self.coord[1] += distance_y
        self.coord2[1] += distance_y
        if self.coord2[1] >= 0:
            self.coord[1] = self.y_original
            self.coord2[1] = self.y2_original
