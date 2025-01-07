grossary_list={}

while True:
    try:
        item=input()
    except EOFError:
        break
    else:
        if(item.upper() in grossary_list):
            grossary_list[item.upper()]=grossary_list[item.upper()]+1
        else:
            grossary_list[item.upper()]=1


sortedDict={key: grossary_list[key] for key in sorted(grossary_list)}


for key,val in sortedDict.items():
    print(f"{val} {key}")
