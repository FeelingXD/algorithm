// 연속된 수의 합
import java.util.stream.*;
import java.util.*;
class Solution {
    public int[] solution(int num, int total) {
        if(num%2==1)
            return IntStream.rangeClosed(total/num-num/2,total/num+num/2).toArray();
        else
            return IntStream.rangeClosed(total/num-(num/2-1),total/num+(num/2-1)+1).toArray();
        
    }
}