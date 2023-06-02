n = int(input())
h = list(map(int, input().split(" ")))

answer = 0
h.sort()
num = len(h) - 1

for i in range(0, int(len(h) // 2)):
    answer += h[num - i] * 2
if len(h) % 2 != 0:
    answer += h[num // 2]

print(answer)