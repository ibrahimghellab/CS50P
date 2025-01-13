import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match=re.search(r"^((?:\d){1,3})\.((?:\d){1,3})\.((?:\d){1,3})\.((?:\d){1,3})$",ip)
    if(match):
        for i in range(1,5):
            if(not(int(match.group(i))>=0 and int(match.group(i))<=255)):
                return False

        return True
    return False




if __name__ == "__main__":
    main()
