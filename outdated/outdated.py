month=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def valid_syntaxe(s):
    sFirst=s.split("/")
    sSecond=s.split(" ")

    if(len(sSecond)==3):
        if("," in sSecond[1]):
            sSecond[1]=sSecond[1].replace(",","")
        elif(sSecond[0]==""):
            sSecond.remove("")
        else:
            return ""

    try:
        if(len(sFirst)==3 and int(sFirst[0])<=12 and int(sFirst[1])<=31):
            return str(f"{int(sFirst[2]):04}-{int(sFirst[0]):02}-{int(sFirst[1]):02}")
        elif(len(sSecond)==3 and sSecond[0] in month and int(sSecond[1])<=31):
            return str(f"{int(sSecond[2]):04}-{int(month.index(sSecond[0].title()))+1:02}-{int(sSecond[1]):02}")
        else:
            return ""
    except ValueError:
        return ""


while True:
    date=input("Date: ")
    if(valid_syntaxe(date)!=""):
        print(valid_syntaxe(date))
        break


