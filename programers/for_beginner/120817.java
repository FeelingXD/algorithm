// 피자먹기(4)
import java.util.*;
class Solution {
    public double solution(int[] numbers) {
        double answer=Arrays.stream(numbers).reduce(0,(a,b)->  a + b);
        return answer/numbers.length;
    }
}