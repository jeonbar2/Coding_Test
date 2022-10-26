import java.util.Arrays;
class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        Arrays.sort(numbers);
        int last = numbers.length-1;
        answer= numbers[last]*numbers[last-1];
        return answer;
    }
}