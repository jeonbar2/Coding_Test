n = int(input())
answer = 0
while n != 0:

    if n % 5 == 0:
        n -= 5
        answer += 1

    else:
        n -= 2
        answer += 1
    if n < 0:
        answer = -1
        break
print(answer)
