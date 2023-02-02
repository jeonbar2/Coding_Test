def solution(s):
    answer = 0
    temp =[]
    for i in s.split(' '):
        if i == "Z":
            answer -= int(temp[-1])
        else:
            answer+=int(i)
            temp.append(int(i))
    return answer