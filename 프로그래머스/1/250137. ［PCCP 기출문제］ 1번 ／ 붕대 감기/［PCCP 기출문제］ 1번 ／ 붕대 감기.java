class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        int last = attacks[attacks.length-1][0];
        int temp = 0;
        int heal = 0;
        int max = health;
        
        for(int i = 1; i<=last ;i++){
            if(i == attacks[temp][0]){
                health -= attacks[temp][1];
                temp++;
                heal = 0;
            }
            else {
                if(health+bandage[1]<max){
                    health += bandage[1];
                    heal++;
                }
                else if (health+bandage[1] == max){ 
                    health = max;
                    heal++;
                }
                else {
                    health = max;
                    heal++;
                }
                if(heal == bandage[0]){
                if(health + bandage[2]>=max){
                    health = max;
                    heal = 0;
                } else {
                    heal=0;
                    health += bandage[2];
                }
               
            }
            }
            
            
            if(health<=0) { return -1;}
        }
        
        
        return health;
    }
    
}