//가까운 수
class Solution {
    public int solution(int[] array, int n) {
        int answer=array[0];
        int max=Math.abs(n-array[0]);
        
        for(int num:array){
            if(max>=Math.abs(n-num)){
                if(max==Math.abs(n-num)){
                    answer =   num>answer ? answer :num;
                    continue;
                }
                max=Math.abs(n-num);
                answer=num;
            }
        }
        
        return answer;
    }
}