//중복된 숫자 개수
import java.util.*;
class Solution {
    public int solution(int[] array, int n) {// n = target   
       return (int)Arrays.stream(array).filter(x->x==n).count();
    }
}