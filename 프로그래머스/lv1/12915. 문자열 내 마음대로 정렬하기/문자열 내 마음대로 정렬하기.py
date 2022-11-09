def solution(strings, n):
    answer = []
    strings.sort()
    a={}
    for i in range(0,len(strings)):
        a[i]=strings[i][n]
  
    
    a = sorted(a, key= lambda x : a[x])

    for i in a:
        answer.append(strings[i])
    
    return answer