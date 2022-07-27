n, k = map(int, input().split())
lst=[]
answer=[]
for i in range(1,n+1):
    lst.append(i)

# a=k-1
# while(len(lst)!=0):
#     # print(a)
#     answer.append(str(lst.pop(a)))
#     if(a+k>len(lst)):
#         a+=k-1
#         a-=len(lst)
#     else:
#         a+=k-1
#     if(len(lst)<=a):
#         a-=len(lst)
#
num=0
for i in range(n):
    num+=k-1
    if num>=len(lst):
        num=num%len(lst)
    answer.append(str(lst.pop(num)))
print("<", ", ".join(answer), ">", sep='')