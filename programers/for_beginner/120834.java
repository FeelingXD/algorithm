//외계행성의 나이
import java.util.*;
class Solution {
    public String solution(int age) {
        StringBuilder sb= new StringBuilder();
        while(age>9){
            sb.append((char)(97+age%10));
            age/=10;
        }
        sb.append((char)(97+age));
        return sb.reverse().toString();
    }
}