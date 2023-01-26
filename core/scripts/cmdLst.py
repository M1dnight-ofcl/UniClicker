# IMPORT STUFF
import os
import time
from core.print import head
from core.print import quit
from core.scripts import shop
from core.transition import transFade as fade
from core import setVar as var
from core.shopItm import itm1
from getkey import getkey, keys as key

from getkey import *
from core.shopItm import itm2

def change():
  global score
  score = int(var.score) + 1
  var.score = score

def log(msg):
  log = open('core/log.txt', 'a')
  log.write(str(var.curTime) + ' - ' + msg)
  log.write('\n')
  log.close()

# ACTUAL CODE
def cmdRun():
  ans = input()
  if ans == 'help':
    clear = lambda: os.system('clear')
    clear()
    head.loadHead()
    h1 = open('txt-assets/menu/help.txt', 'r')
    help = h1.read()
    print(help)
    h1.close()
    log('cmd.help has been run')
    cmdRun()
  if ans == 'helpAdv':
    clear = lambda: os.system('clear')
    clear()
    head.loadHead()
    h1 = open('txt-assets/menu/helpAdv.txt', 'r')
    help = h1.read()
    print (help)
    h1.close()
    cmdRun()
  if ans == 'shop':
    clear = lambda: os.system('clear')
    clear()
    head.loadHead()
    h1 = open('txt-assets/menu/shop.txt', 'r')
    help = h1.read()
    print (help)
    h1.close()
    shop.shopRun()
    cmdRun()
  if ans == 'home':
    clear = lambda: os.system('clear')
    clear()
    head.loadHead()
    cmdRun()
  if ans =='reload':
    clear = lambda: os.system('clear')
    clear()
    head.loadHead()
    cmdRun()
  if ans =='quit':
    clear = lambda: os.system('clear')
    clear()
    fade.fadeIn()
    clear = lambda: os.system('clear')
    clear()
    quit.quit()
  if ans == 'set':
    print()
    print('The command you are trying to run is locked for devs only. Type the password below or type "#" to leave')
    pw = input()
    if pw == '#':
      clear = lambda: os.system('clear')
      clear()
      head.loadHead()
      cmdRun()
    if pw == var.pw:
      clear = lambda: os.system('clear')
      clear()
      head.loadHead()
      print()
      print('Password Correct')
      amt1 = input('Insert Ammount Desired ')
      var.score = amt1
      clear = lambda: os.system('clear')
      clear()
      head.loadHead()
      cmdRun()
  if ans == 'give':
    print()
    print('The command you are trying to run is locked for devs only. Type the password below or type "#" to leave')
    pw = input()
    if pw == '#':
      clear = lambda: os.system('clear')
      clear()
      head.loadHead()
      cmdRun()
    if pw == var.pw:
      clear = lambda: os.system('clear')
      clear()
      head.loadHead()
      print()
      print('Password Correct')
      amt1 = input('Insert Ammount Desired ')
      var.score = int(var.score) + int(amt1)
      clear = lambda: os.system('clear')
      clear()
      head.loadHead()
      cmdRun()
    else:
      print('The password you entered is incorrect')
      clear = lambda: os.system('clear')
      clear()
      head.loadHead()
      cmdRun()
  if ans == 'credits':
    clear = lambda: os.system('clear')
    clear()
    head.loadHead()
    h1 = open('txt-assets/menu/credits.txt', 'r')
    help = h1.read()
    print (help)
    h1.close()
    time.sleep(3)
    clear = lambda: os.system('clear')
    clear()
    head.loadHead()
    cmdRun()
  if ans == '':
    clear = lambda: os.system('clear')
    clear()
    change()
    itm1.run1()
    head.loadHead()
    cmdRun()

  else: 
    print('The command you are trying to run command is either invalid or unavaliable at the moment')
    cmdRun()
