def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    return good_size(s) and good_start(s) and good_numeric_position(s) and no_punctuations(s)

def good_size(s):
    return (len(s)<=6 and len(s)>=2)

def good_start(s):
    return s[0:2].isalpha()

def good_numeric_position(s):
    i=0
    found=False
    while(i<len(s)-1 and not found):
        found=s[i].isnumeric()
        i=i+1



    return (s[i-1:len(s)].isnumeric() and int(s[i-1])!=0) or s[i-1:len(s)].isalpha()


def no_punctuations(s):
    punc=[" ",",","?",";",".",":","!"]
    for i in range(len(s)):
        if(s[i] in punc):
            return False
    return True


main()
