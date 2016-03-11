#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        # TODO: Implement...
        return None

    @abstractmethod
    def update(self):
        pass