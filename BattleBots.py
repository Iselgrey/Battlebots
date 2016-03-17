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
        # Initialize pygame engine and set window title...
        pygame.init()
        pygame.display.set_caption('Battle Bots')
        # Object to be used for FPS control...
        self.fps_clock = pygame.time.Clock()
        # Get a surface to draw on...
        self.display_surface = pygame.display.set_mode(self.RESOLUTION)
        # Create each of the games window...
        self.screen_menu = MenuScreen(self.callback, self.RESOLUTION)
        self.screen_game = GameScreen(self.callback, self.RESOLUTION)
        # Set the current window to be the menu...
        self.screen_current = self.screen_menu

    def loop(self):
        # Main loop of the game...
        while True:
            # Let the current screen draw on the surface...
            self.screen_current.draw(self.display_surface)
            # Get all the pygame events (keystrokes, mouse clicks...) and pass them to the current window...
            for event in pygame.event.get():
                self.screen_current.event(event)
            # Notify pygame to refresh the screen...
            pygame.display.update()
            # Control FPS...
            self.fps_clock.tick(self.FPS_TARGET)

    def callback(self, code, opt):
        # This function will be called by the screens and receives events that may change the status of the screen...
        if code == MenuScreen.ACTION_QUIT:
            self.quit()
        elif code == MenuScreen.ACTION_STARTGAME:
            self.screen_current = self.screen_game
            self.screen_game.restart()
        elif code == MenuScreen.ACTION_SETP1:
            self.screen_game.set_p1(opt)
        elif code == MenuScreen.ACTION_SETP2:
            self.screen_game.set_p2(opt)
        elif code == GameScreen.ACTION_STOP:
            self.screen_current = self.screen_menu
        elif code == GameScreen.ACTION_QUIT:
            self.quit()
        else:
            print("[!] Unrecognized action...")
            self.quit()

    def quit(self):
        # Exits the game...
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    b = BattleBots()
    b.loop()
