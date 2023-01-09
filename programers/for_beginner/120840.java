// 구슬을 나누는 경우의 수
import java.math.BigInteger;
class Solution {
    public int solution(int balls, int share) {
        
        BigInteger answer = combination(balls,share);
        return answer.intValueExact();
    }
    public static BigInteger combination(int n,int r ){
        return factorial(n).divide(factorial(r).multiply(factorial(n-r)));
    }
    public static BigInteger factorial(int n) {
		if (n <= 1)

			return BigInteger.ONE;

		BigInteger k = BigInteger.ONE;

		for (int i = 2; i <= n; i++) {

			k = k.multiply(BigInteger.valueOf(i));

		}

		return k;

	}
}