def solution(s):
    answer = [0,0]
    
    while s!='1':
        count=0
        answer[0]+=1
        for i in s:
            if i == '0':
                count+=1
                answer[1]+=1
        s = bin((len(s)-count))[2:]
    return answer