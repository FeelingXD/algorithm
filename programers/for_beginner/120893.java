//대문자와 소문자
class Solution {
    public String solution(String my_string) {
        int step=(int)('a'-'A');
        StringBuilder sb= new StringBuilder();
        for(char c:my_string.toCharArray()){
            if(c<'a'){
                sb.append((char)(c+step));
            }else{
                sb.append((char)(c-step));
            }
        }
        return sb.toString();
    }
}