//숨어있는 숫자의 덧셈(1)
import java.util.*;
class Solution {
    public int solution(String my_string) {
        ArrayList<Integer> answer= new ArrayList<>();
            String numbers = my_string.replaceAll("[^0-9]","");
            for(String s:numbers.split("")){
                answer.add(Integer.parseInt(s));
            }
            return answer.stream().filter(n->n!=null).mapToInt(n->n).reduce(0,(a,b)->a+b);
    }
}