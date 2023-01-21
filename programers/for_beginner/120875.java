//평행
import java.util.*;
class Solution {
    public int solution(int[][] dots) {
        List<Double> li = new ArrayList();
        for(int i=0;i<dots.length;i++){
            for(int j=i+1;j<dots.length;j++){
                 li.add(((double)dots[j][0]-dots[i][0])/((double)dots[j][1]-dots[i][1]));   //x2-x1 / y2-y1
            }
        }
        Set<Double> distinct= new HashSet(li);
        return  li.size()!=distinct.size() ? 1:0;
    }
}