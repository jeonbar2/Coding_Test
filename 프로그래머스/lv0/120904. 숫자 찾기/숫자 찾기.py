def solution(num, k):
    answer = -1
    for i in range(0,len(list(str(num)))):
        if list(str(num))[i]==str(k):
            answer=i+1
            break
    return answer