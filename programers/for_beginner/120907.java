//OX 퀴즈
import java.util.*;
class Solution {
    public String[] solution(String[] quiz) {
        ArrayList<String> answer= new ArrayList<>();
        for(String str:quiz){
            answer.add(calculate(str));
        }
        return answer.stream().toArray(String[]::new);
    }
    public String calculate(String str){
        boolean isMinus=false;
        int sum=0;
        for(String s:str.split(" ")){
            if(s.equals("=")||s.equals("-")){
                isMinus= isMinus ? false:true;
                continue;
            }
            if(!s.equals("+")){
                sum = (isMinus) ? (sum-=Integer.parseInt(s)) : (sum+=Integer.parseInt(s));
                isMinus=false;
            }
        }
        return (sum==0) ? "O":"X";
    }
}