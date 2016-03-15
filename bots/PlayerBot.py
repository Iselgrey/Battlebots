#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame.locals import *
from bots.AbstractBot import AbstractBot

class PlayerBot(AbstractBot):
    SPEED = 10

    def __init__(self):
        super(PlayerBot, self).__init__("Antón", "PlayerBot", "0")
        self.dx = 0
        self.dy = 0

    def update(self, px, py):
        px = px + self.dx
        self.dx = 0
        py = py + self.dy
        self.dy = 0
        return (px, py)

    def event(self, event):
        if event.key == K_UP:
            self.dy = self.dy - self.SPEED
        elif event.key == K_DOWN:
            self.dy = self.dy + self.SPEED
        elif event.key == K_LEFT:
            self.dx = self.dx - self.SPEED
        elif event.key == K_RIGHT:
            self.dx = self.dx + self.SPEED
