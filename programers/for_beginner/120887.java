//k의 개수
import java.util.stream.*;
class Solution {
    public int solution(int i, int j, int k) {
        return (int)IntStream.rangeClosed(i,j).reduce(0,(a,b)->a+(int)Integer.toString(b).chars().filter(c->c==Character.forDigit(k,10)).count());
    }
}