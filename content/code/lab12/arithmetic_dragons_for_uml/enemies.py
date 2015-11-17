# coding: utf-8
# license: GPLv3

from gameunit import *

class Enemy(Attacker):
    pass


class Dragon(Enemy):
    _color = None
    __answer = None
    __quest = None
    def set_answer(self, answer):
        pass

    def check_answer(self, answer):
        pass
    def question(self):
        pass

class GreenDragon(Dragon):
    def question(self):
        pass


class RedDragon(Dragon):
    def question(self):
        pass


class BlackDragon(Dragon):
    def question(self):
        pass
