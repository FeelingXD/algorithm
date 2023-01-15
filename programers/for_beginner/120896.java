// 한 번만 등장한 문자
import java.util.*;
class Solution {
    public String solution(String s) {
        ArrayList<String> answer= new ArrayList();
        for (char c:s.toCharArray()){
            if(s.chars().filter(x -> x == c).count()==1){
                answer.add(Character.toString(c));
            }
        }
        Collections.sort(answer);
        return String.join("",answer);
    }
}