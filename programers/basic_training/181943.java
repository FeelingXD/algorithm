//문자열 겹쳐쓰기
class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        return overWriteString(my_string,overwrite_string,s);
    }
    public String overWriteString(String fs, String os, int index){
            return fs.substring(0,index)+os+fs.substring(index+os.length());
    }
}