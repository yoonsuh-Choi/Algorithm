def solution(myString):
    answer = ''
    myString = myString.lower()
    if 'a' in myString:
        answer = myString.replace('a', 'A')
    else:
        answer = myString
    return answer