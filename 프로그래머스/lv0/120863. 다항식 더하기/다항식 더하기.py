def solution(polynomial):
    answer = ''
    num = 0 #숫자
    temp = 0 #계수
    
    polynomial = polynomial.split() #리스트로 스플릿하기 
    
    for i in polynomial:
        if "x" in i: #계수 뽑아내기
            if len(i) >= 2:
                temp += int(i[:-1])
            else:
                temp += 1
                
        if i.isdigit():
            num += int(i)

    if num == 0:
        if temp != 1:
            answer = f"{temp}x"
        else:
            answer = "x"
            
    elif num != 0:
        if temp == 0:
            answer = f"{num}"
        elif temp ==1:
            answer = f"x + {num}"
        else:
            answer = f"{temp}x + {num}"
    

    return answer
    