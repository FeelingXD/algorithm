import java.util.Scanner;
//문자열 돌리기
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        for(Character c:a.toCharArray()){
            System.out.println(c);
        }
    }
}