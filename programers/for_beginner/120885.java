//이진수 더하기
import java.util.*;
class Solution {
    public String solution(String bin1, String bin2) {
        return toBin(toInt(bin1)+toInt(bin2));
    }
    public int toInt(String str){
        int value=0;
        for(int i=0;i<str.length();i++){
            value+=Character.getNumericValue(str.charAt(str.length()-1-i))*Math.pow(2,i);
        }
        return value;
    }
    public String toBin(int value){
        StringBuilder sb= new StringBuilder();
        while(value>1){
            sb.insert(0,Integer.toString(value%2));
            value/=2;
        }
        sb.insert(0,Integer.toString(value%2));
        return sb.toString();
    }
}