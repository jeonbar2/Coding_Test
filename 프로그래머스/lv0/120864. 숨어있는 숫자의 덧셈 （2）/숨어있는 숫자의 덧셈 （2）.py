def solution(my_string):
    answer = 0
    temp=""
    for i in my_string:
        if i.isdigit():
            temp+=(i)
        else :
            temp+=(' ')
   
    for i in temp.split():
        answer+=int(i)
    return answer