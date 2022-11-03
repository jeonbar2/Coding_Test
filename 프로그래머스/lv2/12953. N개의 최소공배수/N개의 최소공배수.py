def solution(arr):
    answer = 0
    def lcm(a,b):
        ans =a
        ans = a if a>=b else b
        
        for i in range(ans,a*b+1):
            if i%a==0 and i%b==0:
                ans=i
                break
        
        return ans
    answer= lcm(arr[0],arr[1])
    for i in range(2,len(arr)):
        answer = lcm(arr[i],answer)
      
        
    return answer