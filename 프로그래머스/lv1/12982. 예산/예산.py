def solution(d, budget):
    answer = 0
    temp=0
    d.sort()
    for i in d:
        if temp+i<=budget:
            temp+=i
            answer+=1
    return answer