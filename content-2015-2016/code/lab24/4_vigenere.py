__author__ = 'Timofey Khirianov'
# -*- coding: utf8 -*-

class Vigenere:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    
    def __init__(self, keyword):
        self.alphaindex = {self.alphabet[index]: index for index in range(len(self.alphabet))}
        self.key = [self.alphaindex[letter] for letter in keyword.lower()]

    def caesar(self, letter, shift):
        if letter in self.alphaindex:  # строчная буква
            index = (self.alphaindex[letter] + shift)%len(self.alphabet)
            cipherletter = self.alphabet[index]
        elif letter.lower() in self.alphaindex:  # заглавная буква
            cipherletter = self.caesar(letter.lower(), shift).upper()
        else:
            cipherletter = letter
        return cipherletter

    def encode(self, line, key = None):
        if not key:
            key = self.key
        ciphertext = []
        i = 0
        for letter in line:
            shift = key[i]
            cipherletter = self.caesar(letter, shift)
            ciphertext.append(cipherletter)
            i = (i + 1)%len(key)
            
        return ''.join(ciphertext)

    def decode(self, line):
        key = [len(self.alphabet) - shift for shift in self.key]
        return self.encode(line, key)


keyword = input('keyword=')
cipher = Vigenere(keyword)

line = input()
while line != '.':
    print(cipher.encode(line))
    line = input()
