a=input()
# (()[[]])([])
stack =[]
ans = 0
temp=1
for i in range(len(a)):
    if(a[i] == "(" ):
        stack.append(a[i])
        temp*=2
    elif(a[i] == ")"):
        if( not stack or stack[-1]!="(" ):
            ans=0
            break
        if(a[i-1]=="("):
            ans+=temp

        temp//=2
        stack.pop()

    elif (a[i] == "["):
        stack.append(a[i])
        temp*=3
    elif (a[i] == "]"):
        if (not stack or stack[-1] != "["):
            ans = 0
            break
        if (a[i - 1] == "["):
            ans += temp
        temp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(ans)

# 스택에서 pop할때에 원래 리스트랑 비교한후 tmp를 다시 2나3 으로 나눠주는 과정이 핵심