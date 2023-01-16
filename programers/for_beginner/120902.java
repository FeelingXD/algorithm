//문자열 계산하기
class Solution {
    public int solution(String my_string) {
       boolean isMinus=false;
            int sum=0;

            for(String str:my_string.split(" "))
            {
                if(!str.equals("+")&&!str.equals("-")){
                    sum = isMinus ? sum-Integer.parseInt(str):sum+Integer.parseInt(str);
                    isMinus=false;
                    continue;
                }
                if(str.equals("-")){
                    isMinus=true;
                    continue;
                }
            }
            return sum;

        
    
    }
}
