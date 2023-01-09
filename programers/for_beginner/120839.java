// 가위바위보
import java.util.*;
class Solution {
    
    public String solution(String rsp) {
        char[] tmp=rsp.toCharArray();
        StringBuilder sb= new StringBuilder();
        for(char c:tmp){
            if (c=='2'){
                sb.append('0');
            }
            if(c=='0'){
                sb.append('5');
            }
            if(c=='5'){
                sb.append('2');
            }
        }
        return sb.toString();
    }
}