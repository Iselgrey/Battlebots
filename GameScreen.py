#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from AbstractScreen import AbstractScreen
from MisileSprite import MisileSprite

class GameScreen(AbstractScreen):
    ACTION_QUIT = "game_quit"
    color_black = (0, 0, 0)

    def __init__(self, callback_fcn, resolution):
        super(GameScreen, self).__init__(callback_fcn, resolution)
        self.img_tank = pygame.image.load('resources/images/tank.png')
        self.img_tank_180 = pygame.transform.rotate(self.img_tank, 180)
        self.player1_x = 0
        self.player1_y = 0
        self.player2_x = 0
        self.player2_y = 0
        self.restart()
        self.player1_bot = None
        self.player2_bot = None
        self.sprites = []
        self.sprites.append(MisileSprite())

    def set_p1(self, bot):
        self.player1_bot = bot()

    def set_p2(self, bot):
        self.player2_bot = bot()

    def restart(self):
        self.reset = True

    def draw(self, surface):
        surface.fill(self.color_black)
        if self.reset:
            rect = surface.get_rect()
            self.player1_x = rect.centerx-50
            self.player1_y = 0
            self.player2_x = rect.centerx-50
            self.player2_y = rect.height-100
            self.reset = False
        if self.player1_bot != None and self.player2_bot != None:
            #self.player1_x, self.player1_y, foo = self.player1_bot.update(self.player1_x, self.player1_y)
            #self.player2_x, self.player2_y, foo = self.player2_bot.update(self.player2_x, self.player2_y)
            #surface.blit(self.img_tank_180, (self.player1_x, self.player1_y))
            #surface.blit(self.img_tank, (self.player2_x, self.player2_y))
            for s in self.sprites:
                 s.update(self.sprites)
                 s.draw(surface)

    def event(self, event):
        if event.type == QUIT:
            self.action(self.ACTION_QUIT, None)
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                self.action(self.ACTION_QUIT, None)
        elif event.type == KEYDOWN and event.key != K_ESCAPE and self.player1_bot != None and self.player2_bot != None:
            self.player1_bot.event(event)
            self.player2_bot.event(event)
