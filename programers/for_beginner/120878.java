//유한소수 판별하기
import java.util.*;
class Solution {
    public int solution(int a, int b) {
        List<Integer> li= new ArrayList();
        int div = b/gcd(a,b);
        int i=2;
        
        while(div!=1){
            if(div%i==0){
                li.add(i);
                div/=i;
            }
            else
                i++;   
        }
        
        Set<Integer> set = new HashSet<>(li);
        set.remove(2);
        set.remove(5);
        
        return set.size()!=0 ? 2:1;
    }   
    public int gcd(int a, int b){
        int tmp_a = Math.max(a,b);
        int tmp_b = Math.min(a,b);
        
        if(tmp_a%tmp_b ==0){
            return tmp_b;
        }
        
        return gcd(tmp_b, tmp_a%tmp_b);
    }
}
