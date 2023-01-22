//등수 매기기
import java.util.*;
class Solution {
    public Integer[] solution(int[][] score) {
        int[][]tmp=score.clone();
        
        Map<Integer,Integer> table=new HashMap();
        Arrays.sort(score,(a,b)->(b[0]+b[1])-(a[0]+a[1]));
        int i=1;
        for(int[] total:score){
            table.put((total[0]+total[1]),table.getOrDefault((total[0]+total[1]),i));
            i++;
        }
        return Arrays.stream(tmp).map(n->table.get(n[0]+n[1])).toArray(Integer[]::new);
    }
}