def common_char(str1,str2):
    str=""
    for i in str1:
        if i in str2:
            if i not in str:
                str=str+i
    if(str):
        return str.replace(" ","")
    else:
        return "none"

str1="Umuzi"
str2="umula"
common_letters=common_char(str1,str2)
print("Common letters:"+ common_letters)