def solution(numbers, k):
    answer = 0
    temp = []
    
    if (2*k-1) % len(numbers) == 0:
        answer = len(numbers)

    else:
        answer = (2*k-1) % len(numbers)


#     --------------------------내가 푼것-----------------
#     numbers2 = numbers * k #다듬기 필요

#     idx = 0
#     while len(temp) < k:  
#         # idx = idx % len(numbers) #나머지
#         if idx % 2 == 0: #짝수면 공을 던지는 인덱스에 포함이 됨
#             temp.append(numbers2[idx])
#             idx += 1
#         else:
#             idx += 1
#             continue
                    
#     answer = temp[-1]

    return answer