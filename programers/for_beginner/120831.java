//짝수의합
import java.util.stream.IntStream;
class Solution {
    public int solution(int n) {
        return IntStream.rangeClosed(1,n).filter(a->a%2==0).reduce(0,(a,b)->a+b);
    }
}