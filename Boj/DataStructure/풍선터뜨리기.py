#백준 2346번
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
answer=[]
bal = deque(enumerate(map(int, input().split()),start=1)) #인덱스를 1부터 시작하기위해 enumerate랑 start=1을해줌
print(bal)

pang =bal.popleft() #1번풍선 터뜨리기
