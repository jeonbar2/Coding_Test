#문제 백준10828번
## 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성.
import sys

def input():
    return sys.stdin.readline().rstrip()

num = []
N=int(input())

for i in range(N):
    a = input().split()
    if (a[0] == "push"):
        num.append(a[1])

    elif(a[0] == "pop"):
        if(len(num)!=0):
            print(num.pop())
        else:
            print("-1")

    elif(a[0] == "size"):
        print(len(num))

    elif(a[0] == "empty"):
        if(len(num)==0):
            print("1")
        else:
            print("0")

    elif(a[0] == "top"):
        if(len(num)==0):
            print("-1")
        else:
            print(num[-1])


