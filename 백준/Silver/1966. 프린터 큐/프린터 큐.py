import sys
from collections import deque

a= int(input())

for i in range(a):
    num,cur = map(int, input().split())
    important=[]
    important =list(map(int, sys.stdin.readline().split()))
    queue=deque(important)
    count=0
    while queue:
        best = max(queue)
        front =queue.popleft()
        cur-=1
        if(best==front): #가장 중요한게 맨처음
            count +=1
            if cur<0:
                print(count)
                break
        else:
            queue.append(front)
            if cur<0:
                cur= len(queue)-1

