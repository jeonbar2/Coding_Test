def solution(rows, columns, queries):
    answer = []
    matrix = [[(i *columns+j+1 ) for j in range(columns)] for i in range(rows)]
    
    
    from collections import deque
    for i in queries:
        sub_matrix=deque([])
        
        for j in range(i[1]-1,i[3]):
            sub_matrix.append(matrix[i[0]-1][j])
        
        for j in range(i[0],i[2]-1):
            sub_matrix.append(matrix[j][i[3]-1])
        
        for j in range(i[3]-1,i[1]-2,-1):
            sub_matrix.append(matrix[i[2]-1][j])
        
        for j in range(i[2]-2,i[0]-1,-1):
            sub_matrix.append(matrix[j][i[1]-1])
        
        sub_matrix.appendleft(sub_matrix.pop())
        answer.append(min(sub_matrix))
        
        for j in range(i[1]-1,i[3]):
            matrix[i[0]-1][j]=sub_matrix.popleft()
        for j in range(i[0],i[2]-1):
            matrix[j][i[3]-1]=sub_matrix.popleft()
        for j in range(i[3]-1,i[1]-2,-1):
            matrix[i[2]-1][j]=sub_matrix.popleft()
        for j in range(i[2]-2,i[0]-1,-1):
            matrix[j][i[1]-1]=sub_matrix.popleft()
        
    return answer