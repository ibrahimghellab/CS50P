
def main():
    fraction=input("Fraction: ")
    percentage=convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    fractionSplited=fraction.split("/")
    try:
        numerator=int(fractionSplited[0])
        denominator=int(fractionSplited[1])
        return round(float(numerator/denominator)*100)
    except (ValueError, ZeroDivisionError,IndexError):
        print("Error on your input")



def gauge(percentage):
    if(percentage>100):
        sys.exit("Too big numbers")
    elif(percentage<=1):
        return "E"
    elif(percentage>=99):
        return "F"
    else:
        return str(round(percentage))+"%"


if __name__ == "__main__":
    main()
