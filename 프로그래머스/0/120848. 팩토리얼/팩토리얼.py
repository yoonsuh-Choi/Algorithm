def solution(n):
    answer = 0
    fac = 1
    i = 1
    while True:
        fac = fac * i
        if fac > n:
            break
        else:
            i += 1
    answer = i - 1
    return answer