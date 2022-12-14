def solution(n):
    answer = 0
    #n과 6의 최소공배수
    for i in range(min(6,n),6*n+1):
        if i%n==0 and i%6==0:
            answer = i//6
            break
    return answer