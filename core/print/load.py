# IMPORTING STUFF
import os
import time
from core import lang as ez

def frame(f):
  f = open('txt-assets/loadScreen/' + str(f) + '.txt', 'r')
  lMsg = f.read()
  print (lMsg)
  f.close()

def load(wt):
  frame(1)
  time.sleep(wt)
  ez.cls()
  frame(2)
  time.sleep(wt)
  ez.cls()
  frame(3)
  time.sleep(wt)
  ez.cls()
  frame(4)
  time.sleep(wt)
  ez.cls()

  