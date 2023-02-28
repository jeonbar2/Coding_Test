n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input())))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
rows, cols = len(grid), len(grid[0])
cnt = 0
count = 0
a = []
for row in range(rows):
    for col in range(cols):
        if grid[row][col] != 1:
            continue

        cnt += 1
        stack = [(row, col)]

        count = 0
        while stack:
            x, y = stack.pop()
            if grid[x][y] != 0:
                count += 1
            grid[x][y] = 0

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != 1:
                    continue
                stack.append((nx, ny))
        a.append(count)

print(cnt)
answer = sorted(a)
for i in answer:
    print(i)
