// 모음 제거
class Solution {
    public String solution(String my_string) {
        String[] collections={"a","e","i","o","u"};
        for(String s:collections){
            my_string= my_string.replace(s,"");
        }
        return my_string;
    }
}