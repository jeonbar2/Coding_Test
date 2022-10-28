def solution(hp):
    answer = 0
    if hp/5>0:
        answer+=int(hp/5)
        hp%=5
        
    if hp/3>0:
        answer+=int(hp/3)
        hp%=3
    
    if hp/1>0:
        answer+=int(hp/1)
        hp%=1
        
    return answer