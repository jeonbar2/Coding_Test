from collections import deque
def solution(A, B):
    answer = -1
    A=deque(A)
    B=deque(B)
    for i in range(0,len(A)):
        if A==B:
            answer = i
            break
        A.appendleft(A.pop())
        
    return answer