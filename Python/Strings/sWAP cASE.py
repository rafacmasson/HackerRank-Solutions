def swap_case(s):
    swap = ""
    
    for i in s:
        if i.isupper():
            swap += i.lower() # Uppercase letters converted to lowercase letters
        elif i.islower():
            swap += i.upper() # Lowercase letters converted to uppercase letters
        else:
            swap += i
    
    return swap

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)