def solution(num, k):
    answer = 0
    for i in str(num):
        if i == str(k):
            answer = str(num).index(i)+1
            break
        else:
            answer = -1
    return answer