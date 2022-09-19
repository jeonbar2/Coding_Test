k=int(input())
# 입력
# 3
# 1 6 4 3 5 2 7

# 출력
# 3
# 6 2
# 1 4 5 7
tr=list(map(int,input().split()))

ans= [[] for _ in range(k)]
print(ans)

def inorder(tr,depth):
    mid = len(tr)//2
    ans[depth].append(tr[mid])
    if len(tr)==1:
        return
    inorder(tr[:mid:],depth+1)
    inorder(tr[mid+1::],depth+1)

inorder(tr,0)

for i in ans:
    print(*i)
