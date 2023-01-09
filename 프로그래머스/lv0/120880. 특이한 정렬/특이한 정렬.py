def solution(numlist, n):
    answer = []
    return sorted(numlist, key=lambda x: (abs(x-n), -x))