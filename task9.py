def vowel(x): 
    y= {i for i in x.lower() if i in 'a,e,i,o,u'}
    if y:
        print("Vowels:",*y)
    else:
        print("not present")
vowel("HelloUU")