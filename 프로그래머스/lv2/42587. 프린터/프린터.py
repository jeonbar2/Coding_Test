from collections import deque
def solution(priorities, location):
    answer = 1
    stack=[]
    priorities = deque(priorities)
    i=0
    while i<len(priorities):
        
        if priorities[i] == max(priorities):
            if i == location:
                
                break
            elif location-1 >=0: 
                location-=1
            else : 
                location+len(priorities)-1
                 
            
            (priorities.popleft())
            answer+=1
        elif priorities[i]<max(priorities):
            x = priorities.popleft()
            priorities.append(x)
            if location-1>=0:
                location-=1
            else:
                location+=len(priorities)-1

        
        
    return answer