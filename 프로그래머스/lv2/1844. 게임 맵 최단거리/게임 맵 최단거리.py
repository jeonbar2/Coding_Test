def solution(maps):
     # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    m = len(maps[0])
    def bfs(x, y):
        from collections import deque
        q = deque()
        q.append((x, y))

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    q.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
        
        if maps[n-1][m-1] == 1:
            return -1
        return maps[n - 1][m - 1]



    answer = bfs(0,0)
    return answer