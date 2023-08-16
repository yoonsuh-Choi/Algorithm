def solution(quiz):
    answer = []
    
    for strings in quiz:
        st_list = strings.split(" ")
        result = int(st_list[0])
        for i in range(len(st_list)):
            if st_list[i] == "+":
                result += int(st_list[i+1])
            if st_list[i] == "-":
                result -= int(st_list[i+1])
                
            if st_list[i] == "=":
                print(result)
                #다음에 오는 수가 계산이랑 같은지
                if int(st_list[i+1]) == result:
                    answer.append("O")
                else:
                    answer.append("X")
    return answer