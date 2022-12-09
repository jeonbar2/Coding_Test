def solution(age):
    answer = ''
    alp=['a','b','c','d','e','f','g','h','i','j']
    age = str(age)

    for i in age:
        answer+=(alp[int(i)])
    return answer