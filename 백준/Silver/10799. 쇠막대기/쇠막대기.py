#백준 10799번
# () -> 레이져
# (...) ->쇠막대기

arr=input()
stack=[]
answer=0
index = (len(arr))
# for i in arr:
#     if i =="(":
#         stack.append(i)
#     elif i == ")":
#         stack.pop(-1)
#         print("괄호완성")
#         print("남아있는 스택개수")
#         answer+=(len(stack))
for i in range(index):
    if arr[i]== "(":
        stack.append(arr[i])
    elif arr[i]== ")":
        if arr[i-1]=="(":
            stack.pop(-1)
            answer+=len(stack)
        else:
            stack.pop(-1)
            answer+=1
print(answer)

