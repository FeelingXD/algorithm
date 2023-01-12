//주사위의 개수
class Solution {
    public int solution(int[] box, int n) {
        int answer=1;
        for (int i=0;i<box.length;i++){
            if(box[i]<n){
                return 0;
            }
            box[i]=box[i]/n;
            answer*=box[i];
        }
        
        return answer;
    }
}