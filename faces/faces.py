def convert(txt:str):
    result=""
    result = txt.replace(":)","🙂")
    result = result.replace(":(","🙁")
    return result

def main():
    inputVal = input("")
    print(convert(inputVal))



main()
