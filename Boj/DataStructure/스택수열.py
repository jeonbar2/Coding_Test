# 백준 1874번 
import sys
# sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.
# 즉, 인터프리터에 관련한 작업을 할 때 사용하는 모듈
input = sys.stdin.readline
answer  =[]
n = int(input())  # 8 (입력 개수)
arr = [int(input()) for _ in range(n)]  # [4, 3, 6, 8, 7, 5, 2, 1] (입력 배열)
index = 0
stack=[]

for i in range(1,n+1):
    stack.append(i)
    answer.append('+')

    while stack and stack[-1]==arr[index]:
        stack.pop()
        answer.append('-')
        index+=1

if stack:
    print("NO")
else:
    for i in answer:
        print(i)
