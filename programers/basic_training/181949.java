import java.util.*;
// 대소문자 바꿔서 출력하기
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        StringBuilder answer= new StringBuilder();
        for(char c:a.toCharArray()){
           if ('a'<=c && c<='z'){
               answer.append(Character.toUpperCase(c));
           }
            else{
                answer.append(Character.toLowerCase(c));
            }
        }
        System.out.println(answer);
    }
}