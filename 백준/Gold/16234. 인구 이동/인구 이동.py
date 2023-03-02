# n = int(input())
# grid = []
# for i in range(n):
#     grid.append(list(map(int, input())))
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# rows, cols = len(grid), len(grid[0])
# cnt = 0
# count = 0
# a = []
# for row in range(rows):
#     for col in range(cols):
#         if grid[row][col] != 1:
#             continue

#         cnt += 1
#         stack = [(row, col)]

#         count = 0
#         while stack:
#             x, y = stack.pop()
#             if grid[x][y] != 0:
#                 count += 1
#             grid[x][y] = 0

#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != 1:
#                     continue
#                 stack.append((nx, ny))
#         a.append(count)
#         for i in grid:
#             print(i)
#         print("***********************")

# print(cnt)
# answer = sorted(a)
# for i in answer:
#     print(i)
from collections import deque
import sys

input = sys.stdin.readline
N, L, R = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(i, j):
    q = deque([])
    q.append((i, j))
    nation = []
    nation.append((i, j))
    while q:
        (x, y) = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(A[nx][ny] - A[x][y]) <= R:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    nation.append((nx, ny))

    return nation


cnt = 0
isTrue = True
while isTrue:
    visited = [[0] * N for i in range(N)]
    isTrue = False
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                nation = bfs(i, j)
                if len(nation) > 1:
                    isTrue = True
                    people = sum([A[x][y] for x, y in nation]) // len(nation)
                    for x, y in nation:
                        A[x][y] = people
    cnt += 1

print(cnt-1)
