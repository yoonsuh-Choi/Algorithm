def solution(a, d, included):
    answer = 0
    list_num = []
    for i in range(len(included)):
        list_num.append(a+i*d)
        if included[i]==True:
            answer+= list_num[i]
    return answer