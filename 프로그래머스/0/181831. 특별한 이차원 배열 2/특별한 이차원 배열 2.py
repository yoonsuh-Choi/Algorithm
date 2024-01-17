def solution(arr):
    answer = 0
    for i in range(len(arr)): #0, 1, 2
        for j in range(len(arr)):
            if arr[i][j]==arr[j][i]:
                answer = 1
                continue
            else:
                answer = 0
                break
        break
                        
    return answer