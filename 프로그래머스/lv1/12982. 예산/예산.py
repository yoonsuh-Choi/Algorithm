def solution(d, budget):
    answer = 0
    sums = 0
    for i in d:
        sums += i
    while sums > budget:
        if sums > budget:
            sums -= max(d)
            d.remove(max(d))
            answer = len(d)
    if sums <= budget:
        answer = len(d)
    print(d)
    return answer