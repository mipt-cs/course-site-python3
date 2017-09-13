# coding: utf-8
# license: GPLv3

from gameunit import *

class Hero(Attacker):
    def __init__(self, name):
        self._experience = 0
        self._name = name

    def attack(self, target):
        self._experience += self._attack
