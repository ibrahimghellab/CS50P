input= input("")
inputSplited=input.split(" ")
result=""+inputSplited[0]
for i in range(1,len(inputSplited)):
    result=result+"..."+inputSplited[i]

print(result)
