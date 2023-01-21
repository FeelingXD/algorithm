//겹치는 선분의 길이
import java.util.*;
class Solution {
    public int solution(int[][] lines) {
            int[] li=new int[200];
            for(int[] line:lines){
                for(int i=line[0]+100;i<line[1]+100;i++){
                    li[i]+=1;
                }
            }
            return (int)Arrays.stream(li).filter(n->n>=2).count();
        }
    }