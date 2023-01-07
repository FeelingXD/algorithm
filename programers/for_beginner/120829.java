//각도계산
class Solution {
    public int solution(int angle) {
        if (angle/90==0)
            return 1;
        else if (angle/90==1)
            return angle%90!=0 ? 3:2;
        return 4;
    }
}