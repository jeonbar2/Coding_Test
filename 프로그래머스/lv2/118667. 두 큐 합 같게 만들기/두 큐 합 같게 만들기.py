from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1= deque(queue1)
    queue2= deque(queue2)
    a= len(queue1)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    temp = sum1+sum2
    if temp%2==1:
        answer = -1    
    else:
        while sum1 != sum2:
            
            if sum1>sum2:
                t = queue1.popleft()
                queue2.append(t)
                sum1 -= t
                sum2 += t
            elif sum2>sum1:
                t= queue2.popleft()
                queue1.append(t)
                sum2 -= t
                sum1 +=t
            
            if answer > (a)*2+1:
                answer = -1
                break
            answer+=1
    return answer