def count_substring(string, sub_string):
    # Counter for the number of times that the substring occurs in the string
    counter = 0
    
    for i in range(len(string)):
        # Checking if this part of the string is equal to the substring
        if string[i:i+len(sub_string)] == sub_string:
            counter += 1
    
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)