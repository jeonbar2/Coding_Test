#백준 2346번
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
answer=[]
bal = deque(enumerate(map(int, input().split()),start=1)) #인덱스를 1부터 시작하기위해 enumerate랑 start=1을해줌
ans = []

while bal:
    idx, paper = bal.popleft()
    ans.append(idx)
    if paper>0:
        bal.rotate(-(paper-1))
    else:
        bal.rotate(-(paper))

print(' '.join(map(str, ans)))


# # enumerate 사용
# enumerate 사용 전
# deque([3, 2, 1, -3, -1])
# enumerate 사용 후
# deque([(0, 3), (1, 2), (2, 1), (3, -3), (4, -1)])
# # rotate함수 사용,
# deque.rotate()
# rotate(-1)은 원형 큐를 반시계방향으로 1칸 회전시키고, rotate(1)은 시계방향으로 1칸 회전시킨다고 생각하면 쉽다.