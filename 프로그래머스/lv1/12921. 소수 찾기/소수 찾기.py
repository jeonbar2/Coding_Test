import math
def solution(n):
    answer = 0
    array=[True for i in range(n+1)] # 0,1을 제외한 모든 숫자가 소수(True)인 것으로 설정하고 시작한다.
    
# # 에라토스테네스의 체 알고리즘
#     for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인
# 	    if array[i]==True:	# i가 소수인 경우
#     	# i를 제외한 i의 모든 배수를 지우기
#             j=2
#             while i * j<=n:
#         	    array[i*j]=False
#                 j+=1
    for i in range(2, int(math.sqrt(n))+1):
        if array[i]==True:
            j=2
            while i*j <= n:
                array[i*j]=False
                j+=1

    answer = array.count(True)
    return answer-2