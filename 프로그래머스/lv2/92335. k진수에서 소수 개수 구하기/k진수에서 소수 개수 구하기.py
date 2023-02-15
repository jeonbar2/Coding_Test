def solution(n, k):
    def sosu(p):
        if p<=1:
            return False
        for i in range(2, int(p**0.5)+1):
            if p%i==0:
                return False
        return True
    answer = 0
    # 일단 n을 k 진수로 바꾸자
    # 437674를 3 진수로 바꾸면 -> 211020101011
    temp = []
    while n>k:
        temp.append(n%k)
        n=n//k
    if n!=0:
        temp.append(n)
    temp = temp[::-1]
    
    stack=0
    for i in temp:
        if i == 0:
            if stack:
                if sosu(stack): 
                    answer+=1
                
            stack=0
        else:
            stack=stack*10+i
    if sosu(stack):
        answer+=1
    return answer