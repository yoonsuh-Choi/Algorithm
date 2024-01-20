def solution(my_string):
    answer = 0
    temp = ''
    for idx, i in enumerate(my_string):
        
        if i.isdigit(): # i가 숫자라면 
            temp += i
        else: #숫자가 아니면 
            if temp != '':
                answer += int(temp)
                temp = ''
    if temp != '':
        answer += int(temp)
    return answer