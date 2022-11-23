def solution(my_str, n):
    answer = []
    for i in range(0,len(my_str)//n):
        answer.append(my_str[i*n:i*n+n])
    if my_str[len(my_str)//n*n:]:
        answer.append(my_str[len(my_str)//n*n:])
    return answer