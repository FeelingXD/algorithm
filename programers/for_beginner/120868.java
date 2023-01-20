//삼각형의 완성조건(2)
class Solution {
    public int solution(int[] sides) {
        return sides[0]+sides[1]-(Math.max(sides[0],sides[1])-Math.min(sides[0],sides[1]))-1;
    }
}