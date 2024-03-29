import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maze = []

for _ in range(n):
    maze.append(
        list(map(int, input().rstrip()))
    )  # readline의 경우 맨 뒤에 '\n'까지 입력받으므로 제거해줘야 함

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                q.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1
    return maze[n - 1][m - 1]


print(bfs(0, 0))

## bfs로 지나가는길을 전에 지나온길 +1을 해준다
