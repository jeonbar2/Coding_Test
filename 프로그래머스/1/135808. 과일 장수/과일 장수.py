def solution(k, m, score):
    answer = 0
    number_box=(len(score)//m)
    score.sort(reverse = True)

    for i in range(0,number_box):
        answer+=(score[i*m+(m-1)]*m)
    return answer