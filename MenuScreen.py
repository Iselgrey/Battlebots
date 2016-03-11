#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from AbstractScreen import AbstractScreen

class MenuScreen(AbstractScreen):
    ACTION_QUIT = "menu_quit"
    ACTION_STARTGAME = "menu_startg"
    COLOR_BLACK = (  0,   0,   0)
    COLOR_WHITE = (255, 255, 255)

    def __init__(self, callback_fcn):
        super(MenuScreen, self).__init__(callback_fcn)
        self.font = pygame.font.SysFont("monospace", 15)
        self.label_top = self.font.render("Main menu", 1, self.COLOR_WHITE)

    def draw(self, surface):
        surface.fill(self.COLOR_BLACK)
        surface.blit(self.label_top, (100, 100))

    def event(self, event):
        if event.type == QUIT:
            self.action(self.ACTION_QUIT, None)
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                self.action(self.ACTION_QUIT, None)
            elif event.key == K_SPACE:
                self.action(self.ACTION_STARTGAME, None)
            elif event.key == K_UP:
                pass
            elif event.key == K_DOWN:
                pass
            elif event.key == K_LEFT:
                pass
            elif event.key == K_RIGHT:
                pass
