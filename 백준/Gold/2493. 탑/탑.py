n = int(input())
top = list(map(int, input().split()))
stack=[]
ans=[]
for i in range(0,n):
    while stack:
        if stack[-1][1]>top[i]: 
            ans.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack: 
        ans.append(0)

    stack.append([i, top[i]])
print(" ".join(map(str, ans)))

