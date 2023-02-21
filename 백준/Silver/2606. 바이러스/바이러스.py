computers = int(input())
nodes = {}
for i in range(1, computers + 1):
    nodes[i] = []

m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    nodes[x].append(y)
    nodes[y].append(x)


visited = []
stack = [1]

while stack:
    pre = stack.pop()

    if pre not in visited:
        visited.append(pre)
    for next in nodes[pre]:  # 다음 인접 노드 방문
        if next not in visited:  # 방문 하지 않았으면
            stack.append(next)  # 스택에 추가

print(len(visited) - 1)
