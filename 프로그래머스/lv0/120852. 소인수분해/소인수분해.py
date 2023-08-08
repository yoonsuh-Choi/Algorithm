def solution(n):
    answer = []
    
    i = 2    
    while True :
        if n % i == 0: #나누어 떨어지면 
            n= n//i #몫을 가져온다
            answer.append(i)

        if n % i != 0: #더이상 나누어 떨어지지 않을때 
            i += 1 #i에 1 추가해줌

        if n == 1:
            break
    answer = sorted(list(set(answer)))
    return answer