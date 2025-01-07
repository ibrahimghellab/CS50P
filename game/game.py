import random

while True:
    try :
        lvl=int(input("Level: "))
        rand=random.randint(1,lvl)
        break
    except (ValueError,IndexError):
        pass


found=False
while not found:
    try:
        guess=int(input("Guess: "))
        if(guess>rand):
            print("Too large!")
        elif(guess<rand):
            print("Too small!")
        else:
            print("Just right!")
            found=True
    except ValueError:
        pass
