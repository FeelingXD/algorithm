//n의배수 고르기
import java.util.*;

class Solution {
    public int[] solution(int n, int[] numlist) {
        ArrayList<Integer> answer= new ArrayList<>();
        for(int i=0;i<numlist.length;i++){
            if(numlist[i]%n==0)
                answer.add(numlist[i]);
        }
        return answer.stream().mapToInt(x->x).toArray();
    }
}
