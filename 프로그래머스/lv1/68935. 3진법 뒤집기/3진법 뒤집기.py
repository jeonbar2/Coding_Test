def solution(n):
    answer = 0
    a=''
    
    print(a)
    while n!=0:
        a+=str(n%3)
        n//=3
    
    for i in range(0,len(a)):
        answer+=int(a[i])*3**(len(a)-1-i)
    return answer