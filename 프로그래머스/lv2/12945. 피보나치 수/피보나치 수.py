
def solution(n):
    answer = 0
    temp =0 
    fibo=[1,2]
    for i in range(3,n+1):
        fibo.append(fibo[i-2]+fibo[i-3])
    
    answer = fibo[-2]%1234567
    return answer