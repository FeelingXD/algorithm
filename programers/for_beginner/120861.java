//캐릭터의 좌표
import java.util.*;
class Solution {
   final HashMap<String,int[]> keys = new HashMap();
    public int[] solution(String[] keyinput, int[] board) {
        keys.put("left",new int[]{-1,0});
        keys.put("right",new int[]{1,0});
        keys.put("up",new int[]{0,1});
        keys.put("down",new int[]{0,-1});
        int[] answer= new int[2];
        for(String key:keyinput){
            answer=move(key,answer,board);
        }
        return answer;
        
    }
    public int[] move(String key,int[] cur,int[] board){
        for(int i=0;i<cur.length;i++)
           cur[i] = keys.get(key)[i]+cur[i]<0 ? Math.max(keys.get(key)[i]+cur[i],-1*(board[i]/2)):Math.min(keys.get(key)[i]+cur[i],board[i]/2);
        return cur;            
    }
        
}