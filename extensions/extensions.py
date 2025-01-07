txt = input("File name : ")

txtSplited=txt.split(".")

ext=txtSplited[len(txtSplited)-1]

ext=ext.replace(" ", "")

match ext.lower() :
    case "gif":
        print("image/gif")
    case "jpg"|"jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
