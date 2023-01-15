// 약수 구하기
import java.util.*;
class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> answer=new ArrayList();
        for(int i=1;i<=n/2;i++){
            if(n%i==0){
                answer.add(i);
            }
        }
        answer.add(n);
        
        return answer.stream().mapToInt(x->x).toArray();
    }
}