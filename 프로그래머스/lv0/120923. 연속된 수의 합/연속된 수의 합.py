def solution(num, total):
    answer = []
    mid = (total//num)
    if num %2==0:
        for i in range(mid-int(num/2)+1,mid+int(num/2)+1):
            answer.append(i)
    else:
        for i in range(mid-int(num/2),mid+int(num/2)+1):
            answer.append(i)
    return answer