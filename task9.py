def vowel(x): 
    y= {i for i in x.lower() if i in 'a,e,i,o,u'}
    a=",".join(y)
    if y:
        print("Vowels:",*a)
    else:
        print("not present")
vowel("HelloUU")