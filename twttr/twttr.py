txt=input("Input: ")
txtSplited=list(txt)

for i in range(len(txtSplited)):
    if(txtSplited[i].lower()=="a" or txtSplited[i].lower()=="e" or txtSplited[i].lower()=="i" or txtSplited[i].lower()=="o" or txtSplited[i].lower()=="u"):
        txtSplited[i]=""
    output="".join(txtSplited)

    print(output)
