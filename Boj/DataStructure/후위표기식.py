# ex = input()
#
# for i in ex:
#     if i =="+" or i == "-" or i == "/" or i == "*":
#
# 1. ()를 확인
# 2. *, / 인지 확인 후 먼저 들어온 같은 우선순위에 있는 *,/는 문자열에 추가
# 3. 현재 문자는 스택에 추가
# 4. +, - 인지 확인 자신보다 우선순위가 높은 것 문자열에 추가
# 5. )를 확인 () 사이에 모든 연산자를 문자열에추가 
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
        elif i == "+" or i == "-":
            while stack and stack[-1] != "(":
                ans+=stack.pop()
            stack.append(i)
        elif i==")":
            while stack and stack[-1] != "(":
                ans+= stack.pop()
            stack.pop()
while stack :
    ans+= stack.pop()
print(ans)
