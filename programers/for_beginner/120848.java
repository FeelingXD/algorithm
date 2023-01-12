//팩토리얼
class Solution {
    public int solution(int n) {
        int answer = 0;
        int sum=1;
        for(int i=1;i<=10;i++){
            sum*=i;
            if(sum>n)
                break;
            answer=i;
        }
        return answer;
    }
}