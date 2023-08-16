def solution(my_string):
    st_list = my_string.split(" ")
    answer = int(st_list[0])
    
    for i in range(len(st_list)):
        if st_list[i] == "+":
            answer += int(st_list[i+1])
            
        if st_list[i] == "-":
            answer -= int(st_list[i+1])
            
    return answer