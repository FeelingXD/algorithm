//피자나눠먹기 1
class Solution {
    public int solution(int n) {
        int q= n/7;
        int r= n%7;
        return r==0 ? q:q+1;
    }
}