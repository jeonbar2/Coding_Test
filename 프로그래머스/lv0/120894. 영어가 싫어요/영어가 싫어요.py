def solution(numbers):
    answer = 0
    a= ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    temp=''

    for i in numbers:
        temp+=i
        if temp in a:
            answer*=10
            answer += (a.index(temp))
            temp=''
    return answer