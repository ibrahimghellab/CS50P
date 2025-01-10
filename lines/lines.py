import sys
nbLine=0
try:
    name=sys.argv[1]
except IndexError:
    sys.exit("Too few command-line arguments")
else:
    try:
        error=sys.argv[2]
    except IndexError:
        if(not ".py" in sys.argv[1]):
            sys.exit("Not a Python file")
        try:
            with open(sys.argv[1]) as file:
                for line in file:

                    lineSplited=list(line)
                    while(" " in lineSplited):
                        lineSplited.remove(" ")

                    if(not lineSplited[0]=="#" and not lineSplited[0]=="\n"):
                        nbLine+=1
            print(nbLine)


        except FileNotFoundError:
            sys.exit("File does not exit")

    else:
        sys.exit("Too many command-line arguments")
