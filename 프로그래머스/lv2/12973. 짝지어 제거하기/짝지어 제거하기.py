def solution(s):
    answer = 0
    stack = [] 
    for i in range(0,len(s)):
        if not stack:
            stack.append(s[i])
        elif stack[-1]==s[i]:
            stack.pop()
        elif stack[-1]!=s[i]:
            stack.append(s[i])
        
       
    if not stack:
        answer=1
        
            
    return answer