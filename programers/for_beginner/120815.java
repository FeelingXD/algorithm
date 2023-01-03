//피자 나눠먹기2
class Solution {
    public int solution(int n) {
        
        int q=n/6;
        int r=n%6;
        int pizza=q*6;
        while(r!=0){
            pizza+=6;
            r=pizza%n;
        }
        q=pizza/6;
        return q;
    }
}