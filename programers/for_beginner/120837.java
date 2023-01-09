//개미군단
class Solution {
    public int solution(int hp) {
        int answer = 0;
        int[] ants={5,3,1};
        for(int attack : ants){
            answer+=hp/attack;
            if(hp%attack==0){
                return answer;
            }
            else
                hp=hp%attack;
        }        
        return answer;
    }
}