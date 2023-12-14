import java.util.*;
class Solution {
    public int solution(String s) {
        int answer = 0; 
        for(int i = 0 ;i<s.length();i++){
            // System.out.println(s);
            if(perfectClose(s)){
                answer++;
            }
            
            s = s.substring(1).concat(s.substring(0,1));
        }
        
        return answer;
    }
    public boolean perfectClose(String s){
        
        String open = "({[";
        String close = ")}]";
        Stack<String> stack = new Stack<>();
        
        for(int i = 0 ;i<s.length();i++){
            if(open.contains(""+s.charAt(i))){
                  stack.push(""+s.charAt(i));
            }
            else{
                if (stack.isEmpty()){
                    return false;
                }
                if(open.indexOf(stack.pop()) != close.indexOf(""+s.charAt(i))){
                    return false;
                }
            }
          
                     
         }
       
        if(stack.isEmpty()){
            return true;
        }else{
            return false;
        }
        
    }
}