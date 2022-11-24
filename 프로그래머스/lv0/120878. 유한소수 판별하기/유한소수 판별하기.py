def solution(a, b):
    answer = 1
    temp = min(a,b)
    for i in range(temp,0,-1):
        if a%i==0 and b%i==0:
            temp=i
            break
    b= b//temp
    # 2로 나눠지면 나누고 5로 나눠지면 나누고
    while b!=1:
        if b%2==0:
            b=b//2
        if b%5==0:
            b=b//5
        if b%5!=0 and b%2!=0 and b!=1:
            answer = 2
            break
    return answer