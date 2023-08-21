def solution(my_str, n):
    answer = []
    
    start = 0
    end = n
    
    while True:
        
        if end < len(my_str):
            answer.append(my_str[start:end])

            start = end
            end += n
            
        else: #길이를 넘어가면 
            answer.append(my_str[start:len(my_str)])
            # if len(my_str) // n == len(answer):
            break
        
        
    return answer