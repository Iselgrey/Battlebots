#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class AbstractScreen():
    __metaclass__ = ABCMeta

    def __init__(self, callback_fcn, resolution):
        self.callback_fcn = callback_fcn
        self.resolution = resolution

    def action(self, code, opt):
        self.callback_fcn(code, opt)

    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def event(self, event):
        pass
