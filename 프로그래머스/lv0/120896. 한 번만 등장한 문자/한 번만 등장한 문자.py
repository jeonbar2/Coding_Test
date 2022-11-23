def solution(s):
    answer = ''
    s= list(s)
    s.sort()
    
    a= list(set(s))
    a.sort()
    
    for i in a:
        if s.count(i)==1:
            answer+=i
    return answer