from collections import defaultdict

n= int(input())
tr=defaultdict(list)
for i in range(1,n):
    a,b=map(int,input().split())
    tr[a].append(b)
    tr[b].append(a)

answer=[0]*(n-1)

stack=[1]

while stack:
    cur=stack.pop()

    for node in tr[cur]:
        if node == answer[cur-2]:
            continue
        answer[node-2]=cur
        stack.append(node)
for i in answer:
    print(i)
