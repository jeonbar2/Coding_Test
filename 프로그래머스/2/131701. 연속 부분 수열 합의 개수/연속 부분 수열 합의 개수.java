import java.util.*;
class Solution {
    public int solution(int[] elements) {
        int answer = 0;
        HashSet<Integer> set = new HashSet<Integer>();
        int[] elements2 = new int[elements.length*2];
        for(int i=0 ; i< elements2.length ; i++){
            if (i<elements.length){
                elements2[i]=elements[i];                
            }else{
                elements2[i] = elements[i%elements.length];
            }
        }
        
        for(int i = 0 ; i<elements.length ; i++){
            int temp = 0;
            for(int j = i ; j<i+elements.length;j++){
                temp += elements2[j];
                set.add(temp);
            }
        }
        answer = set.size();
        return answer;
    }
}