def solution(spell, dic):
    answer = 0
    for i in dic:
        temp=[]
        a=True
        for j in i:
            if j in spell:
                temp.append(j)
            else:
                a=False
                break
        
        
        if a :
            temp.sort()
            spell.sort()
            if temp==spell:
                answer+=1
    if answer ==0:
        answer = 2
    else:
        answer = 1
                
    return answer