// 저주의 숫자 3
class Solution {
    public int solution(int n) {
        int[] table= new int[n+1];
        table[0]=0;
        for (int i=1;i<=n;i++){
            table[i]= denyThree(table[i-1]+1);
        }
        
        return table[n];
    }
    public int denyThree(int n){
        if(n%3==0||Integer.toString(n).contains("3")){
            return denyThree(n+1);
        }
        return n;
    }
}