def solution(age):
    answer = ''
    alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    age = str(age)

    for i in age:
        answer+=(alp[int(i)])
    return answer