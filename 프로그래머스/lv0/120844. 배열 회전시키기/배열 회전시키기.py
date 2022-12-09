from collections import deque
def solution(numbers, direction):
    answer = []
    numbers = deque(numbers)
    if direction == "left":
        numbers.append(numbers.popleft())
    else:
        numbers.appendleft(numbers.pop())
    answer = list(numbers)
    return answer