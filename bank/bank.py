txt= input("Greeting : ")

if("hello" in txt.lower()):
    print("$0")
elif(txt[0:1].lower()=="h"):
    print("$20")
else:
    print("$100")
