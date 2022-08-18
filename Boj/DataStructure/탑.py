n = int(input())
top = list(map(int, input().split()))
stack=[]
ans=[]
for i in range(0,n):
    while stack:
        if stack[-1][1]>top[i]: # 송신할 탑이 있다면
            ans.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack: #스택이 비어있다면 즉 송신할수없다
        ans.append(0)

    stack.append([i, top[i]])
print(" ".join(map(str, ans)))

