def solution(triangle):
    answer = 0
    
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j==0 :
                triangle[i][j]+= triangle[i-1][j]
                
            elif j==i:
                triangle[i][j] += triangle[i - 1][j-1]
            else:
                triangle[i][j] += triangle[i - 1][j - 1] if triangle[i - 1][j - 1] > triangle[i - 1][j] else triangle[i-1][j]
    answer=max(triangle[len(triangle)-1])
    return answer