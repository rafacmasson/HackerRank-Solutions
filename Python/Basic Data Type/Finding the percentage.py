if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # Summing the values of the student name provided
    summ = 0
    
    for i in student_marks[query_name]:
        summ += i
    
    # Calculating the average and printing it with 2 decimal places
    avg = summ / 3
    print(f"{avg:.2f}")