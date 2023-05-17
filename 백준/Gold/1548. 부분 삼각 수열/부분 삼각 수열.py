N=int(input())

nums=list(map(int,input().split()))
nums.sort()

answer=1

for x in range(N-1):
    for z in range(N-1,-1,-1):
            if z<x+1:
                continue
            if nums[x]+nums[x+1]>nums[z]:
                answer=max(z-x+1,answer)



print(answer)