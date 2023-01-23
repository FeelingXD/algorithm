//치킨 쿠폰
class Solution {
    public int solution(int chicken) {
        int coupon=chicken;
        int answer=0;
        while(coupon>=10){
            answer+=coupon/10;
            int tmp=coupon%10;
            coupon/=10;
            coupon+=tmp;
        }
        return answer;
    }
}