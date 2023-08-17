def solution(name, yearning, photo):
    answer = []
    
    for i in range(len(photo)):
        score = 0
        for idx, j in enumerate(name): #이름에 있는 애가
            if j in photo[i]: #사진에 있으면 
                score += yearning[idx]
        answer.append(score)
                
                
    return answer