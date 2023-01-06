def solution(sides):
    answer = 0
    sides.sort()
    #새로 들어오는게 가장 큰 경우
    
    i= sides[1]+1
    while i<sum(sides):
        answer+=1
        i+=1
    #가장큰 경우가 아닌경우
    i=sides[1]-sides[0]+1
    while sides[1]<sides[0]+i and i<=sides[1]:
        answer+=1
        i+=1
    return answer