#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bots.AbstractBot import AbstractBot

class PlayerBot(AbstractBot):
    def __init__(self):
        super(PlayerBot, self).__init__("Antón", "PlayerBot", "0")

    def update(self):
        return None
