def solution(balls, share):
    answer = 1
    #ball c share
    for i in range(0,share):
        answer*=balls-i
        answer/=i+1
    
    return answer