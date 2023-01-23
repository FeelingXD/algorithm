//문자열 밀기
import java.util.*;
class Solution {
    public int solution(String A, String B) {
        for(int i=0;i<=A.length();i++){
            if(A.equals(B))
                return i;
            A=rotate(A);
        }
        return -1;
    }
    
    public String rotate(String str){
        StringBuilder sb= new StringBuilder();
        sb.append(str.charAt(str.length()-1)); 
        sb.append(str.substring(0,str.length()-1));
        return sb.toString();
    }
}
