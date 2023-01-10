//배열 회전시키기
class Solution {
    public int[] solution(int[] numbers, String direction) {
        int tmp;
        if(direction.equals("right")){
            tmp=numbers[numbers.length-1];
            for(int i=numbers.length-1;0<i;i--){
                numbers[i]=numbers[i-1];
            }
            numbers[0]=tmp;
        }
        else{
            tmp=numbers[0];
            for(int i=0;i<numbers.length-1;i++){
                numbers[i]=numbers[i+1];
            }
            numbers[numbers.length-1]=tmp;
        }
        return numbers;
    }
}