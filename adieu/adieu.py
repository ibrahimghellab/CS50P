allName=[]
while True:
    try:
        txt=input("Name: ")
        allName.append(txt)
    except EOFError:
        break

output_str="Adieu, adieu, to "
if(len(allName)==1):
    print(output_str+allName[0])
elif(len(allName)==2):
    print(output_str+allName[0]+" and "+allName[1])
else:
    for i in range(0,len(allName)-1):
        output_str+=(allName[i]+", ")
    output_str+=("and "+allName[len(allName)-1])

    print(output_str)
