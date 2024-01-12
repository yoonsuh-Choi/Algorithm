def solution(num_list):
    sums=0
    mul = 1
    for i in num_list:
        mul *= i
        sums += i
    if sums**2 > mul:
        return 1
    else:
        return 0
