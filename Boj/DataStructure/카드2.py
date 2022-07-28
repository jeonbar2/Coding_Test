# 백준 2164번 카드2
from collections import deque

n = int(input())

card = [i for i in range(1,n+1)]
card=deque(card)
while len(card)!=1:
    card.popleft()
    card.append(card.popleft())

print(card[0])