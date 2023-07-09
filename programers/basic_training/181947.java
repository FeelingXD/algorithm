import java.util.Scanner;
//덧셈식 출력하기
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println(String.format("%d + %d = %d",a,b,a+b));
    }
}