//최빈값 구하기 
import java.util.*;
class Solution {
    public int solution(int[] array) {
        HashMap<Integer,Integer> dict= new HashMap<>();
        for(int num:array)
            dict.put(num, dict.getOrDefault(num,0)+1);
        
        int result=0;
        int cnt=0;
        int max = Collections.max(dict.values());
        for (int key : dict.keySet()) {
			if (dict.get(key) == max) {
				cnt++;
				result = key;
			}
		}
        return cnt==1 ? result:-1;
    }
}