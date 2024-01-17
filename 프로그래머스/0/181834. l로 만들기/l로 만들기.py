def solution(myString):
    answer = ''
    before_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    for i in myString:
        if i in before_l:
            answer += 'l'
        else:
            answer += i
    return answer