if __name__ == '__main__':
    arr = []
    
    N = int(input())
    
    for i in range(N):
        command = input().split()
        
        if len(command) == 3:
            if command[0] == "insert":
                arr.insert(int(command[1]), int(command[2]))
        elif len(command) == 2:
            if command[0] == "remove":
                arr.remove(int(command[1]))
            elif command[0] == "append":
                arr.append(int(command[1]))
        elif len(command) == 1:
            if command[0] == "print":
                print(arr)
            elif command[0] == "sort":
                arr.sort()
            elif command[0] == "pop":
                arr.pop()
            elif command[0] == "reverse":
                arr.reverse()
