//영어가 싫어요
class Solution {
    public long solution(String numbers) {
        long answer = 0;
        String[] strs={"zero","one","two","three","four","five","six","seven","eight","nine"};
        for(int i=0;i<strs.length;i++){
            numbers=numbers.replace(strs[i],Integer.toString(i));
        }
        return Long.parseLong(numbers);
    }
}