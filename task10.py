def common_letters(str1,str2):
    result=''
    for x in str1.lower():
        for y in str2.lower():
            if x ==y and x not in result:
                result +=x
    return 'Common Letters:' + ", ".join(result)
str1= "gOntse"
str2="fOuntsd"
print(common_letters(str1,str2))