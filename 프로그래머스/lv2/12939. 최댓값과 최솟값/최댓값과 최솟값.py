def solution(s):
    answer = ''
    temp =(s.split(' '))
    
    temp = list(map(int,temp))
    answer+=str(min(temp))
    answer+=' '
    answer+=str(max(temp))
    return answer