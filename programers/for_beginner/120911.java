// 문자열 정렬하기 (2)
import java.util.*;
class Solution {
    public String solution(String my_string) {
        char[] answer = my_string.toLowerCase().toCharArray();
        Arrays.sort(answer);
        return new String(answer);
    }
}