// 콜라문제
class Solution {
    public int solution(int a, int b, int n) { //콜라문제
        long answer=0;
        long bottle = n;
            var tmp_exchange=0;
        while (bottle >= a){
            tmp_exchange=(int)bottle/a;
            bottle=bottle%a;
            answer+=tmp_exchange*b;
            bottle+=tmp_exchange*b;
        }
        return (int)answer;
    }
}