#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class AbstractSprite():
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_aabb(self):
        pass

    @abstractmethod
    def set_pos(self, x, y):
        return False

    @abstractmethod
    def set_angle(self, a):
        return False

    @abstractmethod
    def draw(self, surface):
        return False

    def collides(self, sprites):
        aabb = self.get_aabb()
        for s in sprites:
            if aabb.colliderect(s.get_aabb()) and self != s:
                return True
        return False

