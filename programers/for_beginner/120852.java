//소인수 분해
import java.util.ArrayList;
class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> primes= new ArrayList();
        ArrayList<Integer> answer=new ArrayList();
        int i= 2;
        while (i<=n){
            if (n%i==0){
                primes.add(i);
                n=n/i;
            }else
                i++;
        }
        
        for(int prime:primes){
            if(!answer.contains(prime))
                answer.add(prime);
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}