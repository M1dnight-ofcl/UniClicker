import time
import os
from core.scripts import cmdLst
from core.print import head
from core import setVar as var

# setup for loop
global looping
looping = True 

def run():
  var.score = int(var.score) + (1 * var.amt2)
  time.sleep(1)
  clear = lambda: os.system('clear')
  clear()
  head.loadHead()