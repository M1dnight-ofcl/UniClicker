import os
import time
from math import *
from core.color import color

def ex(ex,x):
  print(ex)
  time.sleep(x)
  clear = lambda: os.system('clear')
  clear()

def cls():
  clear = lambda: os.system('clear')
  clear()
