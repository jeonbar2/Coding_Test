import java.util.PriorityQueue;
import java.util.Collections;

class Solution {
  
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        PriorityQueue<Integer> awards = new PriorityQueue<>(); // 우선순위 큐로 구현
        for(int i = 0 ; i<score.length;i++){
            if(awards.size()<k){
                awards.add(score[i]);
            }else{
                awards.add(score[i]);
                awards.remove();
            }
            answer[i] = awards.peek();
        }
        return answer;
    }
}