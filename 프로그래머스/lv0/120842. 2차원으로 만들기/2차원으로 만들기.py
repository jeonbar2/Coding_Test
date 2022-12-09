def solution(num_list, n):
    answer = []
    temp=[]
    for i in num_list:
        temp.append(i)
        if (len(temp)==n):
            answer.append(temp)
            temp=[]
        
    return answer