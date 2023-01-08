//진료순서 정하기
import java.util.*;
class Solution {
    public int[] solution(int[] emergency) {
        int [] temp = new int[emergency.length];
        int [] answer= new int[emergency.length];
        
        for(int i=0;i<temp.length;i++)
            temp[i]=emergency[i];
        Arrays.sort(temp);
        for(int i=0; i<=emergency.length-1; i++) {
            for(int j=0; j<=emergency.length-1; j++) {
                if(temp[i]==emergency[j]) {
                    answer[j]=emergency.length-i;
                }
            }
        }
        return answer;
    }
}