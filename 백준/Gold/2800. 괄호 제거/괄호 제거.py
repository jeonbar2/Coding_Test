
from itertools import combinations
ex=input()

stack=[]
couple=[]
answer=set()
for idx,i in enumerate(ex):
    if i=="(" :
        stack.append(idx)
    elif i==")":
        start = stack.pop()
        stop = idx
        couple.append([start,stop]) # 알맞은 괄호 쌍을 찾아 index를 저장.

for i in range(1,len(couple)+1):
    combi = combinations(couple,i) #combination을 이용하여 뺴줄 조합의 개수를 구한다.
    for j in combi:
        tmp = list(ex)            #tmp에 원래 식을 저장해주고
        for k in j:               #제거해줄 idx를 ''로 치환해준다.
            start,end = k
            tmp[start] = ''
            tmp[end] = ''
        answer.add(''.join(tmp))

for i in sorted(list(answer)):
    print(i)