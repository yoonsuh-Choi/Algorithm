def solution(n):
    i = 0
    fac = 1
    while n >= fac: #n이 더 클때까지
        i+= 1
        fac *= i 
        print(fac)
    answer = i - 1
    
    return answer