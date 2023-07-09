import java.util.Scanner;
//문자열 붙여서 출력하기
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();
        StringBuilder answer= new StringBuilder();
        answer.append(a);
        answer.append(b);
        System.out.println(answer);
    }
}