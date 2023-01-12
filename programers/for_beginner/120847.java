//최댓값 만들기
import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        Arrays.sort(numbers);
        
        return numbers[numbers.length-1]*numbers[numbers.length-2];
    }
}