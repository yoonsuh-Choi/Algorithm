def solution(start, end):
    answer = []
    
    while True:
        if start == end:
            answer.append(start)
            break
            
        answer.append(start)
        start -= 1
    return answer