def solution(numbers):
    answer = []
    for i in range(0,len(numbers)):
        for j in range(0,i):
            if (numbers[i]+numbers[j]) in answer:
                continue
            else:
                answer.append(numbers[i]+numbers[j])
    
    answer.sort()
    return answer