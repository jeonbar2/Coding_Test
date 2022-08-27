#백준 1620번
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    ans=input().rstrip()
    if ans.isdigit():
        print(dict[int(ans)])
    else:
        print(dict[ans])

#dictionary를 사용용