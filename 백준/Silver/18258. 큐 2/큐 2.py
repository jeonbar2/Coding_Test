#백준 18258번
import sys
from collections import deque


def push(queue, x):
    queue.append(x)

def empty(queue):
    if(len(queue)==0): #큐가 비어있으면
        return 1
    else:
        return 0
def pop(queue):
    if(empty(queue)==1):
        return -1
    else:
        return queue.popleft()
def size(queue):
    return len(queue)

def front(queue):
    if (empty(queue) == 1):
        return -1
    else:
        return queue[0]
def back(queue):
    if (empty(queue) == 1):
        return -1
    else:
        return queue[-1]

input = sys.stdin.readline
queue = deque([])
N = int(input())
for i in range(N):
    a = input().split()
    if(a[0]=="push"):
        push(queue,a[1])
    elif(a[0]=="pop"):
        print(pop(queue))
    elif(a[0]=="size"):
        print(size(queue))
    elif(a[0]=="empty"):
        print(empty(queue))
    elif(a[0]=="front"):
        print(front(queue))
    elif(a[0]=="back"):
        print(back(queue))