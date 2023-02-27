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
