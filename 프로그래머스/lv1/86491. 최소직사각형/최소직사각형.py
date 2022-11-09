def solution(sizes):
    answer = 0
    w=0
    h=0
    for i in sizes:
        i.sort()
        if i[0]>w:
            w=i[0]
        if i[1]>h:
            h=i[1]
    answer= w*h
    return answer