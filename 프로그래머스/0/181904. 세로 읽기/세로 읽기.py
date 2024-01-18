def solution(my_string, m, c):
    answer = ''
    temp = []
    for i in range(len(my_string)):
        if i % m == 0:
            temp.append(my_string[i:m+i])
    for i in temp:
        answer += i[c-1]
    
    return answer