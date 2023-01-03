//분수의 덧셈
class Solution {
    public static int[] solution(int denum1, int num1, int denum2, int num2) {
        int denum3 =denum2*num1+denum1*num2;
        int num3 = num1*num2;
        int gcd = Gcd(num3,denum3);
        int[] answer ={denum3/gcd,num3/gcd};
        return answer;
    }
    public static int Gcd(int a,int b){// 유클리드 호제법
        return (b!=0) ? Gcd(b,a%b) : a;
    }
}