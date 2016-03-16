#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class AbstractSprite():
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_pos(self, x, y):
        return False

    @abstractmethod
    def set_angle(self, a):
        return False

    @abstractmethod
    def draw(self, surface):
        return False
