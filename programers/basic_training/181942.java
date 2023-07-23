import java.util.*;
// 문자열 섞기
class Solution {
    public String solution(String str1, String str2) {
        char[] ca_str1=str1.toCharArray();
        char[] ca_str2=str2.toCharArray();
        StringBuilder answer=new StringBuilder();
        for(int i=0;i<str1.length();i++){
            answer.append(ca_str1[i]);
            answer.append(ca_str2[i]);
        }
        
        return answer.toString();
    }
}