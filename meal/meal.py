def main():
    txt=input("What time is it? ")

    if(convert(txt)<=8 and convert(txt)>=7):
        print("breakfast time")
    elif(convert(txt)<=13 and convert(txt)>=12):
        print("lunch time")
    elif(convert(txt)<=19 and convert(txt)>=18):
        print("dinner time")

def convert(time):
    timeSplited=time.split(":")
    return float(float(timeSplited[0])+(float(timeSplited[1])/60))


if __name__ == "__main__":
    main()
