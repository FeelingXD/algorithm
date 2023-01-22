//로그인 성공?
import java.util.*;
class Solution {
    public String solution(String[] id_pw, String[][] db) {
        Map<String,String> table= new HashMap();
        
        for(String[] data:db){
            table.put(data[0],data[1]);
        }
        System.out.print(table);
        
        return (table.containsKey(id_pw[0])) ? id_pw[1].equals(table.get(id_pw[0])) ? "login":"wrong pw":"fail";
        
        
    }
}