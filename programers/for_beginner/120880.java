//특이한 정렬
import java.util.stream.IntStream;

class Solution {
    public Integer[] solution(int[] numlist, int n) {
    
        return IntStream.of(numlist).boxed().sorted((a,b)->Math.abs(n-b)==Math.abs(n-a)? b-a : Math.abs(n-a)-Math.abs(n-b)).toArray(Integer[]::new);
    }
}