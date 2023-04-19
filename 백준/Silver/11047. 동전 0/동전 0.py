n, m = map(int, input().split(" "))
coin = []
for _ in range(n):
    coin.append(int(input()))
coin = sorted(coin, reverse=True)

ans = 0
for i in coin:
    if m // i >= 1:
        ans += m // i
        m = m % i
print(ans)
