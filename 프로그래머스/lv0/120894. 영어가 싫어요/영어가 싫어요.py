def solution(numbers):
    answer = ''
    
    num_list = ["zero","one","two","three","four","five","six", "seven","eight","nine"]

    for i in num_list:
        if i in numbers:
            numbers = numbers.replace(i, str(num_list.index(i)))
            
    return int(numbers)