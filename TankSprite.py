#!/usr/bin/env python
# -*- coding: utf-8 -*-

from AbstractSprite import AbstractSprite

class TankSprite(AbstractSrite):
    def __init__(self):
        super(TankSprite, self).__init__()

    def set_pos(self, x, y):
        return True

    def set_angle(self, a):
        return True

    def draw(self, surface):
        return True
