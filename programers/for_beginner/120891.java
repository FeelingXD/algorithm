//369 게임
class Solution {
    public int solution(int order) {
        String tmp=Integer.toString(order);
        tmp=tmp.replaceAll("[^369]","");
        return tmp.length();
    }
}