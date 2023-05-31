def solution(n):
    answer = 0
    one_cnt = bin(n).count("1")
    for num in range(n+1,1000001):
        num_one_cnt = bin(num).count("1")
        
        if one_cnt == num_one_cnt:
            answer = num
            break
    return answer