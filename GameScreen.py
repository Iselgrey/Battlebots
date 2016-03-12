#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from AbstractScreen import AbstractScreen

class GameScreen(AbstractScreen):
    ACTION_QUIT = "game_quit"
    color_black = (0, 0, 0)

    def __init__(self, callback_fcn, resolution):
        super(GameScreen, self).__init__(callback_fcn, resolution)
	#self.img_tank = pygame.image.load('resources/tank.bmp')
        self.player1_x = 0
        self.player1_y = 0

    def draw(self, surface):
        surface.fill(self.color_black)
        #surface.blit(self.img_tank, (self.player1_x, self.player1_y))

    def event(self, event):
        if event.type == QUIT:
            self.action(self.ACTION_QUIT, None)
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                self.action(self.ACTION_QUIT, None)
            elif event.key == K_UP:
                self.player1_y -= 5
            elif event.key == K_DOWN:
                self.player1_y += 5
            elif event.key == K_LEFT:
                self.player1_x -= 5
            elif event.key == K_RIGHT:
                self.player1_x += 5
