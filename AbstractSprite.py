#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import pygame
from abc import ABCMeta, abstractmethod

class AbstractSprite():
    __metaclass__ = ABCMeta

    def __init__(self):
        self.__frames = []
        self.__state = 0
        self.__frame = 0
        self.__angle = 0
        self.__aabb = None

    def add_state(self):
        state = len(self.__frames)
        self.__frames.append([])
        return state

    def add_frame(self, state, frame):
        self.__aabb = frame.get_rect()
        self.__frames[state].append(frame)

    def set_state(self, state):
        self.__state = state
        self.__frame = 0

    def get_pos(self):
        return self.__aabb.center

    def set_pos(self, x, y):
        self.__aabb.center = (x, y)

    def get_angle(self):
        return self.__angle

    def set_angle(self, angle):
        # Calculate the delta of angle and update angle
        da = self.__angle - angle
        self.__angle = angle
        # Update the images
        oldpos = self.__aabb.center
        for i in range(len(self.__frames)):
            for j in range(len(self.__frames[self.__state])):
                self.__frames[i][j] = pygame.transform.rotate(self.__frames[i][j], da)
        self.__aabb = self.__frames[0][0].get_rect()
        self.__aabb.center = oldpos

    def draw(self, surface):
        # Draw the frame
        surface.blit(self.__frames[self.__state][self.__frame], self.__aabb)
        # Update the frame
        self.__frame += 1
        if self.__frame >= len(self.__frames[self.__state]):
            self.__frame = 0
        # TODO: Debug code ahead!
        pygame.draw.rect(surface, (255,0,0), self.__aabb, 1)

    def get_aabb(self):
        return self.__aabb

    def collides(self, sprites):
        for s in sprites:
            if self.__aabb.colliderect(s.get_aabb()) and self != s:
                return True
        return False

    @abstractmethod
    def update(self, sprites):
        pass
