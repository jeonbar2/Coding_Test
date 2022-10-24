class Solution {
     public static int getGCD(int num1, int num2) {
        if (num1 % num2 == 0) {
            return num2;
        }
        return getGCD(num2, num1%num2);
    }
    public int[] solution(int denum1, int num1, int denum2, int num2) {
        int[] answer = {0,0};
        int child = denum1 * num2 + denum2 * num1;  // 1 * 4 + 3 * 2 =  10
        int mom = num1* num2;                       // 2 * 4 = 8
        
       
        int gcd = getGCD(mom,child);
        answer[0] = child / gcd;
        answer[1] = mom / gcd;
        return answer;
    }
}