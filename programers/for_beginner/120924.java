//다음에 올 숫자
class Solution {
    public int solution(int[] common) {
        if(common[2]-common[1]==common[1]-common[0])// 등차 체크
            return common[common.length-1]+common[2]-common[1];
        else
            return common[common.length-1]*common[2]/common[1];
    }
}
