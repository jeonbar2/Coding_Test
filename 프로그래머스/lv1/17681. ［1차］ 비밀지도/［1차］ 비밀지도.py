def solution(n, arr1, arr2):
    answer = []
    x=[]
    y=[]
    for i in arr1:
        a=''
        temp = i
        for j in range(0,n):
            if temp % 2 == 0 :
                a+="0"
            else:
                a+="1"
            temp = temp//2
        
        x.append(a[::-1])
    for i in arr2:
        a=''
        temp = i
        for j in range(0,n):
            if temp % 2 == 0 :
                a+="0"
            else:
                a+="1"
            temp = temp//2
        
        y.append(a[::-1])
        
    for i in range(0,n):
        asd=''
        for j in range(0,n):
            if x[i][j] == '1' or y[i][j]=='1':
                asd+='#'
            else:
                asd+=' '
        answer.append(asd)
    return answer