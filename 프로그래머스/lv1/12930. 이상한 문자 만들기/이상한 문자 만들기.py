def solution(s):
    answer = ''
    a = s.split(" ")
    x=[]
    for i in a:
        for j in range(0,len(i)):
            if j%2==0:
                answer+=(i[j].upper())
            else:
                answer+=(i[j].lower())
        x.append(answer)
        answer=''
    answer=" ".join(x)
    
    return answer