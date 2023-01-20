//숨어있는 숫자의 덧셈(2)
import java.util.*;
class Solution {
    public int solution(String my_string) {
        int answer=Arrays.stream(my_string.split("[a-zA-Z]")).filter(x->!x.equals("")).mapToInt(Integer::new).reduce(0,(a,b)->a+b);
        return answer;
    }
}