def solution(num_list, n):
    answer = []
    
    len_answer = len(num_list) // n
    
    
    for i in range(len_answer):
        answer.append(num_list[i*n: n*(i+1)])
        # print(answer)
    
    
    return answer