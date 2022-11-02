from collections import deque
def solution(s):
    answer = 0
    s=deque(s)  
    stack=[]
    open=["[","(","{"]
    close=["]",")","}"]
    for j in range(0,len(s)):
        #print(s)
        stack=[]
        a=True
        for i in s:
            if i in open:
                stack.append(i)
            elif i in close :
                if stack and stack[-1] == open[close.index(i)]:
                    stack.pop()
                else:
                    a=False
                    break
        if stack:
            a=False
       
        if a:
            answer+=1
        s.append(s.popleft())
        print(a)
                
            
    return answer