//삼각형의 완성조건(1)
import java.util.*;
class Solution {
    public int solution(int[] sides) {
        int[] tmp=sides;
        Arrays.sort(tmp);
        return tmp[2]>=tmp[1]+tmp[0]? 2:1;
    }
}
