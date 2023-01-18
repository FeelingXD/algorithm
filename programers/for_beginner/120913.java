//잘라서 배열로 저장하기
import java.util.*;
class Solution {
    public String[] solution(String my_str, int n) {
        String[] answer = new String[ my_str.length()%n==0 ? my_str.length()/n: my_str.length()/n+1];
        int idx=0;
        for(int i=0;i<my_str.length();i+=n){
            answer[idx++]=my_str.substring(i,Math.min(i+n,my_str.length()));
        }
        return answer;
    }
}