def solution(s):
    answer = ''
    temp = []
    # 각 문자가 나오는 횟수
    
    for i in s:
        if s.count(i) == 1:
            temp.append(i)
    answer = "".join(sorted(temp))
    return answer