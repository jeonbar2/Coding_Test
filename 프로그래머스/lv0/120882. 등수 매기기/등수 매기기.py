def solution(score):
    answer = []
    a=[]
    for i in score:
        a.append(sum(i)/2)
    li=sorted(a,reverse=True)
 
    for i in a:
        answer.append(li.index(i)+1)
    return answer