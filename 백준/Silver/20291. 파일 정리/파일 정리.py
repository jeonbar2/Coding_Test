n = int(input())
ex = {}
for i in range(n):
    a = input().split(".")[1]
    if not a in ex:
        ex[a] = 1
    else:
        ex[a] += 1

sorted_file = sorted(ex.items())
for k, v in sorted_file:
    print(k.rstrip(), v)