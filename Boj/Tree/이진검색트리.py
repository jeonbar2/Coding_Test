# 입력 : 트리 전위순회      출력 : 트리 후위순회
#       50                       5
#       30                       28
#       24                       24
#       5                        45
#       28                       30
#       45                       60
#       98                       52
#       52                       98
#       60                       50

# 노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
# 노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.

# 전위 순회 : 루트 왼쪽 오른쪽
# 후위 순회 : 왼쪽 오른쪽 루트

import sys
sys.setrecursionlimit(10**9)
pre = []

while True: #입력이 있을때 까지만 입력을받는다.
    try:
        pre.append(int(sys.stdin.readline()))
    except:
        break

def post(s, e):
    if s>e:
        return
    mid = e+1

    for i in range(s+1,e+1):
        if pre[s]<pre[i]:
            mid= i
            break

    post(s+1,mid-1)
    post(mid,e)
    print(pre[s])

post(0,len(pre)-1)

# recursion error가 발생해서 setrecursionlimit를 이용해서 재귀 깊이를 늘려줬다.