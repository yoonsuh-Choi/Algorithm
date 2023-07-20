def solution(my_string):
    answer = ''
    moum = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(moum)):
        if moum[i] in my_string:
            my_string = my_string.replace(moum[i], "")
    return my_string