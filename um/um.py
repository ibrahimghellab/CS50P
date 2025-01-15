import re
import sys


def main():
    print(count(input("Text: ")))

def count(s):
    total=0
    match=re.findall(r"(?:^(um)[\W]|[\W](um)[\W]|[\W](um)$|^(um)$)",s.strip().lower())
    print(match)

    for current_tuple in match:
        for value in current_tuple:
            if(value=="um"):
                total+=1

    return total

if __name__ == "__main__":
    main()
