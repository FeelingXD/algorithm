//다항식 더하기
import java.util.*;
class Solution {
    public String solution(String polynomial) {
        String answer;
        String[] arr= polynomial.split(" ");
        int xnum = (int)Arrays.stream(arr).filter(x->x.contains("x")&&!x.equals("x")).map(x-> x.substring(0,x.indexOf("x"))).mapToInt(Integer::parseInt).reduce(0,(a,b)->a+b)+ (int)Arrays.stream(arr).filter(x->x.equals("x")).count();
        int num = (int)Arrays.stream(arr).filter(x-> !x.contains("x") && !x.equals("+")).mapToInt(Integer::parseInt).reduce(0,(a,b)->a+b);
      if(xnum==0){
          answer= (num!=0)? Integer.toString(num):"";
      }else if(xnum==1){
          answer= (num!=0) ? "x + "+Integer.toString(num) : "x";
      }else{
          answer= (num!=0) ? Integer.toString(xnum)+"x + "+Integer.toString(num) : Integer.toString(xnum)+"x";
      }
        return answer;
    }
}