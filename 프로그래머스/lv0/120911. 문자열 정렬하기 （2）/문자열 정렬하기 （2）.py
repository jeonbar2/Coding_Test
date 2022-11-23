def solution(my_string):
    answer = []
    for i in my_string:
        #print(i.lower())
        # if i.isUpper():
        #     answer +=i.lower()
        answer.append(i.lower())
    answer.sort()
    answer = ''.join(answer)
    return answer