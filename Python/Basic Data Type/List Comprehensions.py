if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Using list comprehension to create a list with the answers
    new_list = [[i, j, k] for i in range(x+1) for j in range(y+1) \
                for k in range(z+1) if i+j+k != n]

    print(new_list)
    
    # Using multiple loops, the solution would be:
    '''
    newlist = []

    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    newlist.append([i, j, k])

    print(array)
    '''