def solution(numbers, k):
    answer = 0
    temp = []
    #공을 던지는 인덱스 : 0, 2, 4, 6...
    # 1-3-5-1-3-5
    # 1-3-2-1
    
    numbers2 = numbers * k #다듬기 필요

    idx = 0
    while len(temp) < k:  
        # idx = idx % len(numbers) #나머지
        if idx % 2 == 0: #짝수면 공을 던지는 인덱스에 포함이 됨
            temp.append(numbers2[idx])
            idx += 1
        else:
            idx += 1
            continue
            
    print(temp)        
        
    answer = temp[-1]
    return answer