//배열 원소의 길이
import java.util.*;
class Solution {
    public int[] solution(String[] strlist) {
        ArrayList<Integer> answer= new ArrayList();
        for(String s: strlist){
            answer.add(s.length());
        }
        return answer.stream().mapToInt(n->n).toArray();
    }
}