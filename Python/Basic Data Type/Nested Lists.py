if __name__ == '__main__':
    # Score list and records list
    score_list = []
    records = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        # Adding the items on the lists
        score_list.append(score)
        records.append([name, score])
        
    # Sorting the lists
    score_list.sort()
    records.sort()

    # Finding the second lowest score on the list    
    second_lowest = score_list[0]

    for i in score_list:
        if i > score_list[0]:
            second_lowest = i
            break
    
    # Finding the names with the second lowest score and printing them in alphabetical order
    for i in records:
        if i[1] == second_lowest:
            print(i[0])
    