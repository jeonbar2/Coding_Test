import java.util.*;

public class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;
        List<Integer> stack = new ArrayList<Integer>();
        List<Integer> ham = new ArrayList<>(List.of(1, 2, 3,1));
        for(int i : ingredient){
            stack.add(i);
            if(stack.size()>=4){
                if(stack.subList(stack.size()-4,stack.size()).equals(ham)){
                    stack.remove(stack.size()-4);
                    stack.remove(stack.size()-3);
                    stack.remove(stack.size()-2);
                    stack.remove(stack.size()-1);
                    answer ++;
                }
            }

        }
        return answer;
    }
}