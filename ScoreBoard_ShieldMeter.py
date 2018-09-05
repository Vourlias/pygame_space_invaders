# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:34:35 2017

@author: john
"""

#
# ScoreBoard - Score keeping and display
#
import pygame
class ScoreBoard:
    def __init__(self,x,y,font,fontsize):
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont(font,fontsize)
        self.score = 0

    def Change(self, amount):
        self.score += amount

    def Show(self,surface,boolx2):
        if boolx2:
            scoretext = self.font.render("Score x2: "+str(self.score), True, (0,0,255))
        else:
            scoretext = self.font.render("Score: "+str(self.score), True, (0,0,255))

        surface.blit(scoretext,(self.x, self.y))
        
    def GetValue(self):
        return self.score

    def SetValue(self, score):
        self.score = score

#
# ShieldMeter - Keep and display vintage style bar shield meter
#

class ShieldMeter:
    def __init__(self, x, y, maxvalue, warnvalue):
        self.x = x
        self.y = y
        self.maxvalue = maxvalue
        self.currentvalue = maxvalue
        self.warnvalue = warnvalue

    def Show(self, surface , boolimmune):
        if self.currentvalue < self.warnvalue:
            self.shieldcolor = (255,0,0)
        else:
            self.shieldcolor = (0,255,0)
        if boolimmune:
            self.shieldcolor = (0,0,255)
        pygame.draw.rect(surface,self.shieldcolor,(self.x, self.y, self.currentvalue,25))

    def Increase(self, amount):
        self.currentvalue += amount
        if self.currentvalue > self.maxvalue:
            selfcurrentvalue = self.maxvalue

    def Decrease(self, amount):
        self.currentvalue -= amount
        if self.currentvalue < 0:
            self.currentvalue = 0

    def GetValue(self):
        return self.currentvalue

    def SetValue(self,value):
        self.currentvalue = value
        if self.currentvalue > self.maxvalue:
            self.currenvalue = self.maxvalue
        if self.currentvalue < 0:
            self.currentvalue = 0
