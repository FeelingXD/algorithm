// 외계어 사전
import java.util.*;
class Solution {
    public int solution(String[] spell, String[] dic) {
        boolean can=false;
        int answer= 2;
        String[] available= Arrays.stream(dic).filter(x->x.length()==spell.length).toArray(String[]::new);
        
        for(String word: available){
            can =true;
            for(int i=0;i<word.length();i++){
                if(i==word.length()-1 && can &&word.contains(spell[i])){
                    return 1;
                }else{
                    if(!word.contains(spell[i]))
                        can= false;
                }
            }
            
        }
        
        return answer;
   
    }
}