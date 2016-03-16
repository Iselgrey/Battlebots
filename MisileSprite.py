#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import pygame
from pygame.locals import *
from AbstractSprite import AbstractSprite

class MisileSprite(AbstractSprite):
    SPEED = 10
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    def __init__(self):
        super(MisileSprite, self).__init__()
        self.anim_mov = []
        self.anim_mov.append(pygame.image.load('resources/images/misile0.png'))
        self.anim_mov.append(pygame.image.load('resources/images/misile1.png'))
        self.aabb = self.anim_mov[0].get_rect()
        self.anim_now = 0
        self.anim_max = len(self.anim_mov)
        for i in range(self.anim_max):
            self.anim_mov[i].set_colorkey(self.BLACK)
        self.ang = 0
        self.set_pos(0, 0)
        self.set_angle(0)

    def set_pos(self, x, y):
        self.aabb.center = (x, y)
        return True

    def set_angle(self, a):
        # Calculate the delta of angle and update angle
        da = math.radians(a) - self.ang
        self.ang = math.radians(a)
        # Update the images
        oldpos = self.aabb.center
        for i in range(self.anim_max):
            self.anim_mov[i] = pygame.transform.rotate(self.anim_mov[i], -math.degrees(da))
        self.aabb = self.anim_mov[0].get_rect()
        self.aabb.center = oldpos
        return True

    def get_aabb(self):
        return self.aabb

    def draw(self, surface, sprites):
        # Update AABB
        self.aabb.centerx += self.SPEED*math.cos(self.ang)
        self.aabb.centery += self.SPEED*math.sin(self.ang)
        # Check for collision
        if self.collides(sprites):
            print("[D] Collision")
        # Update animation
        surface.blit(self.anim_mov[self.anim_now], self.aabb)
        self.anim_now += 1
        if self.anim_now >= self.anim_max:
            self.anim_now = 0
        # TODO: Draw AABB
        pygame.draw.rect(surface, self.RED, self.aabb, 1)
        return True
