def solution(rny_string):
    answer = ''
    temp=''
    for i in rny_string:
        if i == "m":
            answer+="rn"
        else:
            answer+=i
    return answer