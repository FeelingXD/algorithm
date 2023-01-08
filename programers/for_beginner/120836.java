//순서쌍의 개수
class Solution {
    public int solution(int n) {
        int cnt=0;
        for (int i=1;i*i<=n;i++){
            if(i*i==n)
                cnt++;
            else if(n%i==0){
                cnt+=2;
            }
        }
        
        return cnt;
    }
}