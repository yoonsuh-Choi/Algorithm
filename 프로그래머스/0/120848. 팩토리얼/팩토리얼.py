def solution(n):
    answer = 0
    fac = 1
    i = 1
    while fac <= n:
        i += 1
        fac = fac * i
    answer = i - 1
    return answer