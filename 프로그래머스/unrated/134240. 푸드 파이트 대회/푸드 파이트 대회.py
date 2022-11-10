from collections import deque
def solution(food):
    answer = ''
    # 1 3 4 6
    # 1 1 2 3
    # 1 2 2 3 3 3 0 3 3 3 2 2 1
    # 1 7 1 2
    # 1 3 0 1
    # 1 1 1 3 0 3 1 1 1
    for i in range(1,len(food)):
        food[i]=food[i]//2
    
    temp=deque(['0'])
    for i in range(len(food)-1,0,-1):
        for j in range(0,food[i]):
            temp.appendleft(str(i))
            temp.append(str(i))
    temp = list(temp)
    answer = (('').join(temp))
    return answer