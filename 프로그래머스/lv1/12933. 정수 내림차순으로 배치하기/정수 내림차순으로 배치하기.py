def solution(n):
    answer = 0
    temp=[]
    while n>=1:
        temp.append(int(n%10))
        n/=10
    temp.sort(reverse=True)
    
    for i in temp:
        answer*=10
        answer+=i

    return answer