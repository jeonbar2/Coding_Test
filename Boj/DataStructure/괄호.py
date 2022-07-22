# 백준 9012번

N = int(input())
for i in range(N):
    a = input()
    stack=[]
    for j in a:
        if (j=="("):
            stack.append(j)

        elif(j==")"):
            if(len(stack)!=0):
                stack.pop(-1)
            else:
                stack.append("s")
                break
    if(len(stack)==0):
        print("YES")
    else:
        print("NO")

