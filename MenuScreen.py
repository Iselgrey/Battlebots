#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from AbstractScreen import AbstractScreen
from bots.AbstractBot import AbstractBot

class MenuScreen(AbstractScreen):
    ACTION_QUIT = "menu_quit"
    ACTION_STARTGAME = "menu_startg"
    ACTION_SETP1 = "set_p1"
    ACTION_SETP2 = "set_p2"
    COLOR_BLACK = (  0,   0,   0)
    COLOR_WHITE = (255, 255, 255)

    def __init__(self, callback_fcn, resolution):
        super(MenuScreen, self).__init__(callback_fcn, resolution)
        self.bot_list = AbstractBot.list_bots()
        self.bot_p1 = 0
        self.bot_p2 = 0
        self.bot_select = 0
        self.font = pygame.font.Font("resources/fonts/thirteen_pixel_fonts.ttf", 32)
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
        label_p = self.font.render(("> " if self.bot_select == 0 else "  ") + "PLAYER 1: " + self.bot_list.keys()[self.bot_p1], 1, self.COLOR_WHITE)
        label_p_rect = label_p.get_rect()
        label_p_rect.center = rect.centerx, rect.height*18/40
        surface.blit(label_p, label_p_rect)
        label_p = self.font.render(("> " if self.bot_select == 1 else "  ") + "PLAYER 2: " + self.bot_list.keys()[self.bot_p2], 1, self.COLOR_WHITE)
        label_p_rect = label_p.get_rect()
        label_p_rect.center = rect.centerx, rect.height*22/40
        surface.blit(label_p, label_p_rect)

    def event(self, event):
        if event.type == QUIT:
            self.action(self.ACTION_QUIT, None)
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                self.action(self.ACTION_QUIT, None)
            elif event.key == K_SPACE:
                self.action(self.ACTION_SETP1, self.bot_list[self.bot_list.keys()[self.bot_p1]])
                self.action(self.ACTION_SETP2, self.bot_list[self.bot_list.keys()[self.bot_p2]])
                self.action(self.ACTION_STARTGAME, None)
            elif event.key == K_UP:
                self.bot_select = self.bot_select - 1
                if self.bot_select < 0:
                    self.bot_select = 0
            elif event.key == K_DOWN:
                self.bot_select = self.bot_select + 1
                if self.bot_select > 1:
                    self.bot_select = 1
            elif event.key == K_LEFT:
                if self.bot_select == 0:
                    self.bot_p1 = self.bot_p1 - 1
                    if self.bot_p1 < 0:
                        self.bot_p1 = 0
                elif self.bot_select == 1:
                    self.bot_p2 = self.bot_p2 - 1
                    if self.bot_p2 < 0:
                        self.bot_p2 = 0
            elif event.key == K_RIGHT:
                if self.bot_select == 0:
                    self.bot_p1 = self.bot_p1 + 1
                    if self.bot_p1 >= len(self.bot_list)-1:
                        self.bot_p1 = len(self.bot_list)-1
                elif self.bot_select == 1:
                    self.bot_p2 = self.bot_p2 + 1
                    if self.bot_p2 >= len(self.bot_list)-1:
                        self.bot_p2 = len(self.bot_list)-1
