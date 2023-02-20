def solution(my_string):
    answer = 0
    num = 1
    for i in my_string.split(' '):
        if i.isdigit():
            num *= int(i)
            answer += num
        elif i == '-':
            num = -1
        elif i == '+':
            num = 1
            
            
    return answer