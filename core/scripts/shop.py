# IMPORTING OTHER SCRIPTS
from core.scripts import cmdLst
from core.print import head
from core import setVar as var

# IMPORT SHOP ITEM SCRIPTS
from core.shopItm import itm1
from core.shopItm import itm2

# IMPORTING REQUIRED MODULES
import os
import time

# ALTER SETTINGS HERE:
waitTime = 0.6

def relScrn():
    clear = lambda: os.system('clear')
    clear()
    head.loadHead()
    h1 = open('txt-assets/menu/shop.txt', 'r')
    help = h1.read()
    print (help)
    h1.close()
    shopRun()

def shopRun():
  itmNum = input()
  if itmNum == '1':
    if int(var.score) >= 10:
      print('Successfully Bought Auto-Baker')
      var.score = int(var.score) - 10
      var.amt1 = int(var.amt1) + 1
      time.sleep(waitTime)
      relScrn()
    else:
      print('Insuficient Funds')
      time.sleep(waitTime)
      relScrn()
  if itmNum == '2':
    if int(var.score) >= 50:
      print('Successfully Hired Staff')
      var.score = int(var.score) - 50
      var.amt2 = int(var.amt2) + 1
      time.sleep(waitTime)
      relScrn()
    else:
      print('Insuficient Funds')
      time.sleep(waitTime)
      relScrn()
  if itmNum == '3':
    if int(var.score) >= 200:
      print('Successfully Opened Bakery')
      var.score = int(var.score) - 200
      time.sleep(waitTime)
      relScrn()
    else:
      print('Insuficient Funds')
      time.sleep(waitTime)
      relScrn()
  if itmNum == '4':
    if int(var.score) >= 1000:
      print('Successfully Opened Factory')
      var.score = int(var.score) - 1000
      time.sleep(waitTime)
      relScrn()
    else:
      print('Insuficient Funds')
      time.sleep(waitTime)
      relScrn()
  if itmNum == 'x':
    clear = lambda: os.system('clear')
    clear()
    head.loadHead()
    cmdLst.cmdRun()
# commands
  else: 
    print('The command you are trying to run command is either invalid or unavaliable at the moment')
    shopRun()