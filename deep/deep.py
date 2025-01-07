txt=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
txt=txt.replace(" ", "")
match txt.lower():
    case "42"|"fortytwo"|"forty-two":
        print("Yes")
    case _:
        print("No")
