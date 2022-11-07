import math
def solution(n):
    answer = 0
    if n == int(math.sqrt(n))**2:
        answer = (int(math.sqrt(n))+1)**2
    else :
        answer = -1
    return answer