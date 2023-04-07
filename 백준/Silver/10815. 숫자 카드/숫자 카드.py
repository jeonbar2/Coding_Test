import sys

input = sys.stdin.readline
n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
tests = list(map(int, input().split()))
answer = []
for test in tests:
    low, high = 0, n - 1
    check = False
    while low <= high:
        mid = (low + high) // 2
        if cards[mid] == test:
            check = True
            break
        elif cards[mid] < test:
            low = mid + 1
        else:
            high = mid - 1
    print(1 if check else 0, end=' ')
