if __name__ == '__main__':
    s = input()
    
    aln = False
    alph = False
    dig = False
    low = False
    upp = False
    
    for i in s:
        if i.isalnum():
            aln = True
        if i.isalpha():
            alph = True
        if i.isdigit():
            dig = True
        if i.islower():
            low = True
        if i.isupper():
            upp = True
        if (aln == True and alph == True and
            dig == True and low == True and
            upp == True):
            break
            
    print(aln)
    print(alph)
    print(dig)
    print(low)
    print(upp)