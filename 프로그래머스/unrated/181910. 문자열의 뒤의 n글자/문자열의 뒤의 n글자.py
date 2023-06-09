def solution(my_string, n):
    answer = ''
    start = len(my_string)-n
    for i in range(start,len(my_string)):
        answer+=my_string[i]
    return answer