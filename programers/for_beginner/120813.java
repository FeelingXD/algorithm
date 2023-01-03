//짝수는 싫어요
import java.util.*;
class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> arr= new ArrayList<>();
        for(int i=1;i<n+1;i++){
            if (i%2!=0)
                arr.add(i);
        }
        int[] answer= new int[arr.size()];
        int size=0;
        for(Integer num:arr){
            answer[size++]=num.intValue();
        }
        return answer;
    }
}