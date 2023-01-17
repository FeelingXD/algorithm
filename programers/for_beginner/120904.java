//숫자 찾기
class Solution {
    public int solution(int num, int k) {
        int answer = -1;
        String tmp=Integer.toString(num);
        
        for(int i=0;i<tmp.length();i++){
            if(Character.getNumericValue(tmp.charAt(i))==k){
                answer=i+1;
                break;
            }
        }
        return answer;
    }
}