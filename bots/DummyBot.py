#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bots.AbstractBot import AbstractBot

class DummyBot(AbstractBot):
    def __init__(self):
        super(DummyBot, self).__init__("Antón", "DummyBot", "0")

    def update(self, px, py):
        return (px, py)

    def event(self, event):
        pass
