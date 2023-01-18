def solution(s):
    answer = []
    stack={}
    for i in range(0,len(s)):
        if s[i] in stack:
            
            answer.append(i-stack[s[i]])
            stack[s[i]]=i
        else:
            answer.append(-1)
            stack[s[i]]=i
        
    return answer