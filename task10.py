def common_char(str1,str2):
    str=""
    for i in str1.lower():
        if i in str2.lower():
            if i not in str:
                str=str+i
    if(str):
        return str.replace(" ","")
    else:
        return "none"

str1="Umi"
str2="Umla"
common_letters=common_char(str1,str2)
a=", ".join(common_letters)
print("Common letters:"+ a)