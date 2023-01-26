import time
import os
from core.scripts import cmdLst
from core.print import head
from core import setVar as var

def do(amt):
  var.score = int(var.score) + (1 * amt)

def run1():
  do(var.amt1)