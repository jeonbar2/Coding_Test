def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1):
        if str(i) in X and str(i) in Y:
            if i!=0:
                m= min(X.count(str(i)),Y.count(str(i)))
                answer+=str(i)*m
            else:
                if not answer:
                    answer+=str(i)
                else:
                    m= min(X.count(str(i)),Y.count(str(i)))
                    answer+=str(i)*m
                
    if not answer:
        answer="-1"
    
    return answer