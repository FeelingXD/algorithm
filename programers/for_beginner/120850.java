//문자열 정렬하기
import  java.util.*;
class Solution {
    public int[] solution(String my_string) {
      ArrayList<Integer> answer= new ArrayList<>();
            String numbers = my_string.replaceAll("[^0-9]","");
            for(String s:numbers.split("")){
                answer.add(Integer.parseInt(s));
            }
            Collections.sort(answer);
            return answer.stream().filter(n->n!=null).mapToInt(n->n).toArray();
    }
}