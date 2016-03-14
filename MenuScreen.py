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

    def __init__(self, callback_fcn, resolution):
        super(MenuScreen, self).__init__(callback_fcn, resolution)
        self.font = pygame.font.SysFont("monospace bold", 42)
        self.label_top = self.font.render("MAIN MENU", 1, self.COLOR_WHITE)
        self.label_start = self.font.render("PRESS <SPACE> TO START GAME...", 1, self.COLOR_WHITE)

    def draw(self, surface):
        rect = surface.get_rect()
        surface.fill(self.COLOR_BLACK)
        label_top_rect = self.label_top.get_rect()
        label_top_rect.center = rect.centerx, rect.height/4
        surface.blit(self.label_top, label_top_rect)
        label_start_rect = self.label_start.get_rect()
        label_start_rect.center = rect.centerx, rect.height*3/4
        surface.blit(self.label_start, label_start_rect)

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
