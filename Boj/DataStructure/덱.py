#백준 10866번
import sys
from collections import deque


def push_front(dequeue, x):
    dequeue.appendleft(x)

def push_back(dequeue, x):
    dequeue.append(x)

def empty(dequeue):
    if(len(dequeue)==0): #큐가 비어있으면
        return 1
    else:
        return 0
def pop_front(dequeue):
    if(empty(dequeue)==1):
        return -1
    else:
        return dequeue.popleft()

def pop_back(dequeue):
    if(empty(dequeue)==1):
        return -1
    else:
        return dequeue.pop()

def size(dequeue):
    return len(dequeue)

def front(dequeue):
    if (empty(dequeue) == 1):
        return -1
    else:
        return dequeue[0]
def back(dequeue):
    if (empty(dequeue) == 1):
        return -1
    else:
        return dequeue[-1]

input = sys.stdin.readline
dequeue = deque([])
N = int(input())
for i in range(N):
    a = input().split()
    if(a[0]=="push_front"):
        push_front(dequeue,a[1])
    elif(a[0]=="push_back"):
        push_back(dequeue,a[1])
    elif(a[0]=="pop_front"):
        print(pop_front(dequeue))
    elif (a[0] == "pop_back"):
        print(pop_back(dequeue))
    elif(a[0]=="size"):
        print(size(dequeue))
    elif(a[0]=="empty"):
        print(empty(dequeue))
    elif(a[0]=="front"):
        print(front(dequeue))
    elif(a[0]=="back"):
        print(back(dequeue))

