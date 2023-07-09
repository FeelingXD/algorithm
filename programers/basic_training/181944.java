import java.util.Scanner;
//홀짝 구분하기
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(String.format("%d is %s",n,validNumber(n)));
    }
    public static String validNumber(int number){
        return number%2==0? "even":"odd";
    }
}