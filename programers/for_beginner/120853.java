//컨트롤 제트
import java.util.*;
class Solution {
    public int solution(String s) {
        int answer=0;
            Stack<Integer> stack = new Stack();
            for(String str:s.split(" ")){
                if(!stack.isEmpty()&&str.equals("Z")){
                    stack.pop();
                }else if(!s.equals("Z")){
                    stack.push(Integer.parseInt(str));
                }
            }
            while(!stack.isEmpty()){
                answer+=stack.pop();
            }
            
            return answer;
    }
}