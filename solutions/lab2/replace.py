#!/bin/env python3

s = input()

i1 = s.find('h')
i2 = s.rfind('h')

x = s[i1+1:i2].replace('h', 'H')

print(s[:i1+1], x, s[i2:], sep='')