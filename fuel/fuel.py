while True:
    fraction=input("Fraction: ")
    fractionSplited=fraction.split("/")
    if(fractionSplited[0]!=fraction):
        try:
            numerator=int(fractionSplited[0])
            denominator=int(fractionSplited[1])
            result=float(numerator/denominator)*100
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if(result>100):
                pass
            elif(result<=1):
                print("E")
                break
            elif(result>=99):
                print("F")
                break
            else:
                print(str(round(result))+"%")
                break
    else:
        pass









