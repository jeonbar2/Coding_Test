import sys
n = int(input())
circle = []
stack = []
ans="YES"
for i in range(n):
    inp = sys.stdin.readline().split()
    a = int(inp[0])-int(inp[1])
    b = int(inp[0])+int(inp[1])
    circle.append([a,i,0])   # x-r값과 x+r값을 각각 원 번호와 함께 스택에 저장해준다.
    circle.append([b,i,1])   # 처음인지 끝인지 확인하기 위해 0 또는 1을 추가해줬다.
circle.sort()

for i in range(n):
    fir = circle[i][2]
    if fir == 0:
        stack.append(circle[i])
    else:
        if stack[-1][2] == 0:  # 전 원이 닫히지 않은 상태이면
            if stack[-1][1] == circle[i][1]:    #원 번호가 같으면
                stack.pop()
            else:               #원 번호가 다르면 NO를 출력해준다.
                ans="NO"
                break

print(ans)