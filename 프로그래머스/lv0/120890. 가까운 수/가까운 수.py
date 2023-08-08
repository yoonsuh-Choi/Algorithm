def solution(array, n):
    answer = 0
    dis = []
    array = sorted(array)


    for i in array:
        dis.append(abs(n-i))
        idx = dis.index(min(dis)) #차이가 가장 작은 원소의 인덱스
    answer = array[idx] #해당 원소
     
    return answer