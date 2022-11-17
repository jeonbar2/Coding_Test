def solution(s, n):
    answer = ''
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha1="abcdefghijklmnopqrstuvwxyz"
    for i in s:
        if i in alpha1:
            answer+=(alpha1[(alpha1.index(i)+n)%26])
        elif i in alpha:
            answer+=(alpha[(alpha.index(i)+n)%26])
        else:
            answer+=i
        
    return answer