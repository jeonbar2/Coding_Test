def solution(num_list):
    answer = 0
    for i in num_list:
        if i<0:
            break
        answer+=1
    if len(num_list)<=answer:
        answer =-1
    return answer