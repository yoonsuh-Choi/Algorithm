def solution(before, after):
    answer = 0
    for i in before:
        if before.count(i) == after.count(i):
            answer = 1
        else:
            answer = 0
            break

    return answer