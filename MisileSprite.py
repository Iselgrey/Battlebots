#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import pygame
from pygame.locals import *
from AbstractSprite import AbstractSprite

class MisileSprite(AbstractSprite):
    SPEED = 10

    def __init__(self):
        super(MisileSprite, self).__init__()
        self.aabb = Rect(0, 0, 10, 20)
        self.set_pos(0, 0)
        self.set_angle(0)

    def set_pos(self, x, y):
        self.aabb.center = (x, y)
        return True

    def set_angle(self, a):
        self.ang = a
        return True

    def draw(self, surface, sprites):
        self.px += SPEED*math.sin(math.radians(self.ang))
        self.py += SPEED*math.cos(math.radians(self.ang))
        surface.blit(self.aabb, self.aabb, 10)
        return True
