from core import setVar as var

# defining the color class
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def loadHead():
  # prints the logo by retreiving the content of the txt file.
  l1 = open('txt-assets/logo.txt', 'r')
  logo = l1.read()
  print (logo)
  l1.close()

  # the space before my name is to center it under the logo
  print(color.BOLD + '              𝙼𝟷𝚍𝚗𝚒𝚐𝚑𝚝𝙳𝚎𝚟' + color.END)
  print( ) # spacer

  # prints the cookie by retreiving the content of the txt file

  ck1 = open('txt-assets/clickme.txt', 'r')
  clickme = ck1.read()
  print (clickme)
  ck1.close()

  print( ) # spacer
  print('Hello! Welcome to UniClicker' + ', ' + color.BOLD + var.user + color.END + '!')
  print('You Currently Have ' + color.BOLD + str(var.score) + color.END + ' Cookies!')
  print('Type' + color.CYAN + ' Help ' + 
color.END +  'For Help')
