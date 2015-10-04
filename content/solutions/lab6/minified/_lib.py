'''Библиотека для модульного тестирования. Функции этого модуля содержат ошибки, которые требуется найти.'''
import math
def sin(a):
 if a>=-2*math.pi and a<=2*math.pi:
  return math.sin(a)
 else:
  return 0.0
def factorial(n):
 if n<0:
  return-1
 else:
  f=1
  for i in range(2,n+1):
   f*=i
  return float(f)
def even(n):
 if n==0:
  return 0
 elif n>0:
  return n%2==0
 else:
  return False
# Created by pyminifier (https://github.com/liftoff/pyminifier)
