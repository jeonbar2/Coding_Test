def solution(N, stages):
    answer = {}
    temp=0
    a=[]
    n=len(stages)
    for i in range(1,N+1) :
        temp=0
        if n!=0:
            temp+=stages.count(i)/n
            n-=temp*n
            answer[i]=temp
        else:
            answer[i]=0
    #answer = sorted(answer.items())
    sorted_by_value = sorted(answer.items(), key=lambda x: x[1], reverse=True)
    for i in sorted_by_value:
        a.append(i[0])
    return a