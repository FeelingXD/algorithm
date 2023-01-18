//머쓱이보다 키가 큰 사람
import java.util.*;
class Solution {
    public int solution(int[] array, int height) {
        return (int)Arrays.stream(array).filter(x->x>height).count();
    }
}