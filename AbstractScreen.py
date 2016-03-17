#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class AbstractScreen():
    # Abstract class for screen implementations. Every screen should derive from this class...
    # Stores information for sending events to the main class and derived classes should implement how to draw the screen and handle events.
    __metaclass__ = ABCMeta

    def __init__(self, callback_fcn, resolution):
        # Store callback information for sending info to the main class
        self.callback_fcn = callback_fcn
        # Store screen resolution information
        self.resolution = resolution

    def action(self, code, opt):
        # This function sends an action to the main class with a code and an optional parameter
        self.callback_fcn(code, opt)

    @abstractmethod
    def draw(self, surface):
        # Derived class should implement in this function the routines to draw the screen
        pass

    @abstractmethod
    def event(self, event):
        # Derived class should listen to events (key strokes, mouse clicks...) by implementing this class
        pass
