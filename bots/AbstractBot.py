#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bots
import pkgutil
import importlib
from abc import ABCMeta, abstractmethod

class AbstractBot():
    __metaclass__ = ABCMeta

    def __init__(self, author, name, version):
        self.author = author
        self.name = name
        self.version = version

    def get_label(self):
        return self.name + ' v' + self.version + ' by ' + self.author

    @staticmethod
    def list_bots():
        for (module_loader, name, ispkg) in pkgutil.iter_modules(['bots/']):
            importlib.import_module('.' + name, __package__)
        return {cls.__name__: cls for cls in bots.AbstractBot.AbstractBot.__subclasses__()}

    @abstractmethod
    def update(self, px, py):
        pass

    @abstractmethod
    def event(self, event):
        pass
