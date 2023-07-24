import java.util.*;
class Solution {
    //푸드 파이트 대회

    public String solution(int[] food) {
        StringBuilder strbuilder=new StringBuilder();
        for(int i=1;i<food.length;i++){
            int tmp=food[i]/2;
            while (tmp>0){
                strbuilder.append(i);
                tmp--;
            }
        }
        
        List<String> answer=new ArrayList<>();
        answer.add(strbuilder.toString());
        answer.add(reverse(strbuilder));
        
        return String.join("0",answer);        
    }
    public String reverse(StringBuilder str){
        return new StringBuilder(str).reverse().toString();
    }
}