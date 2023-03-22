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

# bracket = list(input())
#
# stack = []
# answer = 0
# tmp = 1
#
# for i in range(len(bracket)):
#
#     if bracket[i] == "(":
#         stack.append(bracket[i])
#         tmp *= 2
#
#     elif bracket[i] == "[":
#         stack.append(bracket[i])
#         tmp *= 3
#
#     elif bracket[i] == ")":
#         if not stack or stack[-1] == "[":
#             answer = 0
#             break
#         if bracket[i-1] == "(":
#             answer += tmp
#         stack.pop()
#         tmp //= 2
#
#     else:
#         if not stack or stack[-1] == "(":
#             answer = 0
#             break
#         if bracket[i-1] == "[":
#             answer += tmp
#
#         stack.pop()
#         tmp //= 3
#
# if stack:
#     print(0)
# else:
#     print(answer)