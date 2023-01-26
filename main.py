# Made by M1dnightDev
# Current version - v1.1.a (alpha)

# IMPORTING STUFF
from datetime import datetime

# IMPORT FROM CORE FOLDER
# import core
from core.scripts import cmdLst as cmd
from core.print import head
from core.color import color
from core.print import quit
from core.scripts import shop
from core.transition import transFade as fade
from core.transition import transSting as sting
from core.print import load
from core import setVar as var
from core.shopItm import itm2

# opening the log file
log = open('core/log.txt', 'a')

# retreive the current date/time
var.curTime = datetime.now()

# logging then game start
log.write(str(var.curTime) + ' - game has started')
log.write('\n')
log.close()

load.load(0.2)
fade.fadeIn()  # main transition
# sting.stingIn() # alternate transition (NOT IN USE, DELETE # TO USE)
head.loadHead()
print()
print(color.RED + color.BOLD + 'Press Enter to Start Baking!' + color.END)
cmd.cmdRun()
