def vowel(x): 
    x="heluulooo"
    y= {i for i in x if i in 'a,e,i,o,u'}
    if y:
        print("Vowels:",*y)
    else:
        print("not present")
vowel(x)