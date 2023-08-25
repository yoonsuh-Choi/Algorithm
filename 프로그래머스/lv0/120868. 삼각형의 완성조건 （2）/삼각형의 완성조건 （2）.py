def solution(sides):
    answer = 0
    case = []
    max_sides = max(sides) #가장 큰 값
    sums_sides = sum(sides) #두변 길이의 합
    dif_sides = abs(sides[0] - sides[1])
    
    for i in range(dif_sides, sums_sides+1):
        #가장 긴변이 sides안에 있을 경우
        # 나머지 한변 : 두 변의 차보다 크고, 자기자신 보다는 작아야 한다
        if i > dif_sides and i <= max_sides:
            case.append(i)

        #나머지 한변이 가장 긴 변인 경우
        # 나머지 한변: sum_sides보다 작고 max_sides보다는 커야한다. 
        if i < sums_sides and i > max_sides:
            case.append(i)

    # print(case)
    answer = len(case)
    return answer