def main():
    txt=input("Greeting: ")
    print(f"$${value(txt)}")


def value(greeting):
    if("hello"==greeting[0:5].lower()):
        return 0
    elif(greeting[0:1].lower()=="h"):
        return 20
    else:
        return 100




if __name__ == "__main__":
    main()

