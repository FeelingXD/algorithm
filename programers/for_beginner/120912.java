//7의 개수
import java.util.*;
class Solution {
    public int solution(int[] array) {
        return Arrays.stream(array).reduce(0,
        (a,b)->a+(int)Integer.toString(b).chars().filter(c->c=='7').count());
    }
}
