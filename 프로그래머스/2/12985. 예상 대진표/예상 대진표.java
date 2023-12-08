class Solution
{
    public int solution(int n, int a, int b)
    {
        a-=1;
        b-=1;
        int answer = 0;
        while(a!=b){ 
            answer+=1;
           
            a/=2;
            b/=2; 
            n/=2;

           
        }
        return answer;
    }
}