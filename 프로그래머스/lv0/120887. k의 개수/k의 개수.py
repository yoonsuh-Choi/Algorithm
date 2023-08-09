def solution(i, j, k):
    answer = 0
    # print(str(i))
    while True:
        if i > j: 
            break
        for num in str(i):
            if num == str(k): #각 자릿수가 k와 같으면 
                answer += 1

        i += 1
    return answer