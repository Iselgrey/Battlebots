#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *
from MenuScreen import MenuScreen
from GameScreen import GameScreen

class BattleBots:
    FPS_TARGET = 30
    RESOLUTION = (1024, 768)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Battle Bots')
        self.fps_clock = pygame.time.Clock()
        self.display_surface = pygame.display.set_mode(self.RESOLUTION)
	self.screen_menu = MenuScreen(self.callback, self.RESOLUTION)
	self.screen_game = GameScreen(self.callback, self.RESOLUTION)
	self.screen_current = self.screen_menu

    def loop(self):
        while True:
            self.screen_current.draw(self.display_surface)
            for event in pygame.event.get():
                self.screen_current.event(event)
            pygame.display.update()
            self.fps_clock.tick(self.FPS_TARGET)

    def callback(self, code, opt):
	if code == MenuScreen.ACTION_QUIT:
            self.quit()
        elif code == MenuScreen.ACTION_STARTGAME:
            self.screen_current = self.screen_game
        elif code == GameScreen.ACTION_QUIT:
            self.screen_current = self.screen_menu

    def quit(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    b = BattleBots()
    b.loop()
