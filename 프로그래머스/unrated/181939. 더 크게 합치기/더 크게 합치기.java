class Solution {
    public int solution(int a, int b) {
        int answer = Integer.valueOf(Integer.toString(a)+Integer.toString(b))
            >= Integer.valueOf(Integer.toString(b)+Integer.toString(a)) ? Integer.valueOf(Integer.toString(a)+Integer.toString(b)):Integer.valueOf(Integer.toString(b)+Integer.toString(a));
        
            
        return answer;
        
    }
}