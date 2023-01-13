// 중복된 문자 제거
import java.util.*;
class Solution {
    public String solution(String my_string) {
        StringBuilder sb = new StringBuilder();
            for(String c:my_string.split("")){
                if(sb.indexOf(c)==-1)
                    sb.append(c);

            }
            System.out.println(sb);
            return sb.toString();
    }
}