if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Turning arr into a list and sorting it descending
    arr = list(arr)
    arr.sort(reverse = True)

    # The runner-up score is the first number on the list smaller than the first one
    runner_up = 0
    
    for i in arr:
        if i < arr[0]:
            runner_up = i
            break
    
    print(runner_up)
    