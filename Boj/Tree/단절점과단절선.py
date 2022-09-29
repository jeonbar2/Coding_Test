from collections import defaultdict
from sys import stdin
n= int(stdin.readline())
tr=defaultdict(list)
edges = [(0, 0)]
for i in range(n-1):
    a,b=map(int,stdin.readline().split())
    tr[a].append(b)
    tr[b].append(a)
    edges.append((a, b))
#트리는 싸이클 구조가 아니기 때문에 루트와 자식이 하나뿐인 노드가 단절점이고 모든 간선이 단절선이다.

q=int(stdin.readline())
for i in range(q):
    t,k = map(int,stdin.readline().split())
    if t==1: # 단절점
        if len(tr[k])>=2:
            print("yes")
        else:
            print("no")
    else:
        print("yes")

# - 단절점(cut vertex) : 해당 정점을 제거하였을 때, 그 정점이 포함된 그래프가 2개 이상으로 나뉘는 경우, 이 정점을 단절점이라 한다.
# - 단절선(bridge) : 해당 간선을 제거하였을 때, 그 간선이 포함된 그래프가 2개 이상으로 나뉘는 경우, 이 간선을 단절선이라 한다.
