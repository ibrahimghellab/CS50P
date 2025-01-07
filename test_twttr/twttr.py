
def main():
    txt=input("Input: ")
    print(shorten(txt))

def shorten(word):
    txtSplited=list(word)

    for i in range(len(txtSplited)):
        if(txtSplited[i].lower()=="a" or txtSplited[i].lower()=="e" or txtSplited[i].lower()=="i" or txtSplited[i].lower()=="o" or txtSplited[i].lower()=="u"):
            txtSplited[i]=""
        output="".join(txtSplited)
    return output


if __name__ == "__main__":
    main()





