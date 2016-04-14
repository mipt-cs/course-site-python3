__author__ = 'Timofey Khirianov'
# -*- coding: utf8 -*-


class Caesar:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, key):
        lowercase_code = {self.alphabet[i]:self.alphabet[(i+key)%len(self.alphabet)] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():self.alphabet[(i+key)%len(self.alphabet)].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        self._decode = {y: x for x, y in self._encode.items()}

    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])

    def decode(self, line):
        if len(line) == 1:
            return self._decode[line] if line in self._decode else line
        else:
            return ''.join([self.decode(char) for char in line])


key = int(input('Введите ключ:'))
cipher = Caesar(key)
line = input()
while line != '.':
    print(cipher.encode(line))
    line = input()