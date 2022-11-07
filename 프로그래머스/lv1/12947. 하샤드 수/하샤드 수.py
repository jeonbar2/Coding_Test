def solution(x):
    answer = True
    a = x
    temp = 0
    while x >=1:
        temp += int(x%10)
        x/=10
  
    if a % temp ==0:
        answer = True
    else:
        answer = False
    return answer