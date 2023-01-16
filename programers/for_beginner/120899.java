//가장 큰수 찾기
class Solution {
    public int[] solution(int[] array) {
        int maxIdx=0;
        int max=0;
        for(int i=0;i<array.length;i++){
            if(array[i]>max){
                max= array[i];
                maxIdx=i;
            }
        }
        return new int[]{max,maxIdx};
    }
}