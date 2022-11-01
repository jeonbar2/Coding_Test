def solution(brown, yellow):
    answer = []
    total = brown+yellow
    x,y=0,0
    
    for i in range(1,(yellow+1)//2+2):
        if yellow%i==0 and brown == 4+(yellow//i+i)*2:
            y=yellow//i
            x=i
                
    answer.append(x+2)
    answer.append(y+2)
    return answer