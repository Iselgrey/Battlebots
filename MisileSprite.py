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
        self.state_normal = self.add_state()
        img = pygame.image.load('resources/images/misile0.png')
        img.set_colorkey((0,0,0))
        self.add_frame(self.state_normal, img)
        img = pygame.image.load('resources/images/misile1.png')
        img.set_colorkey((0,0,0))
        self.add_frame(self.state_normal, img)
        img = pygame.image.load('resources/images/misile2.png')
        img.set_colorkey((0,0,0))
        self.add_frame(self.state_normal, img)
        self.set_pos(0, 0)
        self.set_angle(30)

    def update(self, sprites):
        # Update AABB
        px, py = self.get_pos()
        a = math.radians(self.get_angle())
        px += self.SPEED*math.cos(a)
        py += self.SPEED*math.sin(a)
        self.set_pos(px, py)
        # Check for collision
        if self.collides(sprites):
            # TODO: Go to state 2...
            print("[D] Collision")
        # Keep alive...
        return True
