def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(0,len(A)):
        temp=A[i]*B[len(A)-1-i]
        answer+= temp

    return answer