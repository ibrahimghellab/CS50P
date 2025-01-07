import random
import sys

def main():

    level=get_level()
    good_answer=0
    for _ in range(10):
        error=0
        x=generate_integer(level)
        y=generate_integer(level)
        while error<3:
            try:
                result=int(input(f"{x} + {y} = "))
                if(result==x+y):
                    good_answer+=1
                    break
                else:
                    print("EEE")
                    error+=1
            except ValueError:
                print("EEE")
                error+=1
        if(error==3):
            print(f"{x} + {y} = {x+y}")
    print(f"Score: {good_answer}")


def get_level():
    while True:
        try:
            n=int(input("Level: "))
            print("\n")
            if(n<1 or n>3 ):
                pass
            else:
                return n
        except ValueError:
            pass


def generate_integer(level):
    try:

        match level:
            case 1:
                return random.randint(0,9)
            case 2:
                return random.randint(10,99)
            case 3:
                return random.randint(100,999)
    except ValueError:
        sys.exit("Not an integer")








if __name__ == "__main__":
    main()
