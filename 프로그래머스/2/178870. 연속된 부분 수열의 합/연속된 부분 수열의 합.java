class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = new int[]{0, sequence.length - 1};
//         for (int i=0 ; i<sequence.length; i++){
//             int j=i;
//             int temp =0;
//             while(j<sequence.length && temp < k && j<answer[1]-answer[0]+i){
//                 temp += sequence[j];
//                 if(temp == k ){
//                     answer[0] = i ;
//                     answer[1] = j;
//                 } 
//                 j++;
                
//             }
//         }
        int left = 0;
        int right = 0;
        int total = sequence[0];
        int size = sequence.length;
        while(true){
            if(total == k){
                if(right-left<answer[1]-answer[0]){
                    answer[1]=right;
                    answer[0]=left;
                }
            }
            if(left == size && right == size) break;              
            if(total <=k && right<size){
                right ++;
                if(right<size){total += sequence[right];}
            }
            else {
                if(left<size)total-=sequence[left];
                left ++;
            }  

        }
        return answer;
    }
}