// 문자 반복 출력하기

class Solution {
    public String solution(String my_string, int n) {
        StringBuilder sb = new StringBuilder();
        for(int j =0;j<my_string.length();j++)){
            for(int i=0;i<n;i++){
                sb.append(my_string.charAt(j));
            }
        }
        return sb.toString();
    }
}