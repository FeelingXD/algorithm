//합성수 찾기
class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for(int i=4;i<=n;i++){
            for(int j=2;j<=i/2;j++){
                if(i%j==0){
                    answer+=1;
                    break;
                }
            }
        }
        return answer;
    }
}