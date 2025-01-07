txt = input("Expression : ")
txtSplited=txt.split(" ")

match txtSplited[1]:
    case "+":
        print(round(float(txtSplited[0])+float(txtSplited[2]),1))
    case "-":
        print(round(float(txtSplited[0])-float(txtSplited[2]),1))
    case "*":
        print(round(float(txtSplited[0])*float(txtSplited[2]),1))
    case "/":
        print(round(float(txtSplited[0])/float(txtSplited[2]),1))


