def solution(hp):
    answer, j_num, b_num, i_num = 0, 0, 0, 0
    
    #필요한 장군개미 수 
    j_num  = hp // 5 
    b_num = (hp - j_num*5) // 3
    i_num = hp-j_num*5-b_num*3
    
    answer = j_num + b_num + i_num
    return answer