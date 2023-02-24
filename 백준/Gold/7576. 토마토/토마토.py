import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(m)]

q = deque([])
for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            q.append((i, j))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0


def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                q.append((nx, ny))



bfs()
for i in tomato:
    for j in i:
        if j == 0:
            answer = -1
            print(answer)
            exit(0)
    answer = max(answer, max(i))
print(answer - 1)