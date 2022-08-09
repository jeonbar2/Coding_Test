#백준 10799번
# () -> 레이져
# (...) ->쇠막대기

arr=input()
stack=[]
for i in arr:
    if i =="(":
        stack.append(i)
    elif i == ")":
        stack.pop(-1)
        print("괄호완성")
