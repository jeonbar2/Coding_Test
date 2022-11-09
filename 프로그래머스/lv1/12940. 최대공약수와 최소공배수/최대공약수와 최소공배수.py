def solution(n, m):
    answer = []
    max1 = max(n,m)
    min1 = min(n,m)
    big=0
    small=0
    for i in range(1,min1+1):
        if max1%i==0 and min1%i==0:
            big=i
    answer.append(big)
    
    while max1>0:
        if max1%m==0 and max1%n==0:
            small=max1
            break
        max1+=1
    answer.append(small)
    return answer