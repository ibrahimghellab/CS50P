from pyfiglet import Figlet
import sys
import random

figlet=Figlet()

allFonts=figlet.getFonts()

if((sys.argv[1]=="--font" or sys.argv[1]=="-f") and sys.argv[2] in allFonts):
    inp=input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(inp))
elif(len(sys.argv)==1):
    inp=input("Input: ")
    figlet.setFont(font=allFonts[random.randint(0,len(allFonts)-1)])
    print(figlet.renderText(inp))
else:
    sys.exit("Invalid usage")
