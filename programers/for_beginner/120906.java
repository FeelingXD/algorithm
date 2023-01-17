//자릿수 더하기
class Solution {
    public int solution(int n) {
        int sum=0;
        for(char s:Integer.toString(n).toCharArray())
            sum+=Character.getNumericValue(s);
        return sum;
    }
}