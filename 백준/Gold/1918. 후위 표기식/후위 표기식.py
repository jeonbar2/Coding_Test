# ex = input()
#
# for i in ex:
#     if i =="+" or i == "-" or i == "/" or i == "*":
#
stack=[]
ans=""
ex=input()

for i in ex:
    if i.isalpha():
        ans+=i
    else:
        if i =="(":
            stack.append(i)
        elif i=="*" or i=="/":
            while stack and (stack[-1]=="*" or stack[-1]=="/"):
                ans+=stack.pop()
            stack.append(i)
        elif i=="+"or i=="-":
            while stack and stack[-1]!="(":
                ans+=stack.pop()
            stack.append(i)
        elif i==")":
            while stack and stack[-1] != "(":
                ans+= stack.pop()
            stack.pop()
while stack :
    ans+= stack.pop()
print(ans)
