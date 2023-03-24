n, k = map(int, input().split())
lst=[]
answer=[]
for i in range(1,n+1):
    lst.append(i)

num=0
for i in range(n):
    num+=k-1
    if num>=len(lst):
        num=num%len(lst)
    answer.append(str(lst.pop(num)))
print("<", ", ".join(answer), ">", sep='')