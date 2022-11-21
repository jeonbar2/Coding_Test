def solution(s):
    answer = ''
    
    s = s.split(" ")
    for i in s:
        for j in range(0,len(i)):
            if j==0:
                if not i[j].isdigit():
                    answer+=i[j].upper()
                else :
                    answer+=i[j].upper()
            else:
                answer+=i[j].lower()
        answer+=' '
    answer = answer[:-1]
    
    return answer