txtCamelCase=input("camelCase: ")

temp=list(txtCamelCase)

for i in range(len(temp)):
    if(temp[i]!=temp[i].lower()):
        temp[i]="_"+temp[i].lower()

txt_snake_case="".join(temp)

print(txt_snake_case)
