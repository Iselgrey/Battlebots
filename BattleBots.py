#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *

class BattleBots:
    color_black = (0, 0, 0)

    def __init__(self):
        self.fps_target = 30
        pygame.init()
        self.fps_clock = pygame.time.Clock()
        self.display_surface = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption('Battle Bots')
        self.img_tank = pygame.image.load('resources/tank.bmp')
        self.player1_x = 0
        self.player1_y = 0

    def loop(self):
        while True:
            self.display_surface.fill(self.color_black)
            self.display_surface.blit(self.img_tank, (self.player1_x, self.player1_y))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()
                elif event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        self.quit()
                    elif event.key == K_UP:
                        self.player1_y -= 5
                    elif event.key == K_DOWN:
                        self.player1_y += 5
                    elif event.key == K_LEFT:
                        self.player1_x -= 5
                    elif event.key == K_RIGHT:
                        self.player1_x += 5
            pygame.display.update()
            self.fps_clock.tick(self.fps_target)

    def quit(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    b = BattleBots()
    b.loop()
