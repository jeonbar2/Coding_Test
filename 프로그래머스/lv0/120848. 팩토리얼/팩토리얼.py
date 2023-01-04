def solution(n):
    answer = 1
    def fact(n):
        a=1
        for i in range(1,n+1):
            a*=i
        return a
    i=0
    while fact(i)<=n:
        i+=1
    
    answer = i-1
    return answer