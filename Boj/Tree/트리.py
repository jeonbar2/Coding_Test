n = int(input())
arr=list(map(int,input().split()))
k= int(input())

def dfs(arr,k):
    arr[k]=-10
    for i in range(len(arr)):
        if arr[i]==k:
            dfs(arr,i)
ans=0
dfs(arr,k)
for i in range(len(arr)):
    if i not in arr and arr[i] != -10:
        ans+=1

print(ans)