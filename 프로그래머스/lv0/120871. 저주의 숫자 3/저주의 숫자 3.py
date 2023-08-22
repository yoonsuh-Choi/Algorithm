def solution(n):
    answer = 0
    no_3 = []
    
    for i in range(1, n*3):
        if i % 3 == 0 or "3" in str(i):
            continue
        no_3.append(i)
        
    no_3.sort()
    print(no_3)
    answer = no_3[n-1]
    return answer