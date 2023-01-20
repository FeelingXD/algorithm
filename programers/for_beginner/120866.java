//안전지대
class Solution {
    public int solution(int[][] board) {
        
        int[][] xy={{1,0},{-1,0},{0,1},{0,-1},{-1,1},{1,1},{-1,-1},{1,-1}};
        int[][] tmp= new int[board.length][board[0].length];
        int sum=0;
        for(int x=0;x<board.length;x++){
            for(int y=0;y<board.length;y++){
                if(board[x][y]==1){
                    tmp[x][y]=1;
                    for(int[] around:xy){
                        if(0<=x+around[0]&&x+around[0]<board.length && 0<=y+around[1]&&y+around[1]<board.length){
                            tmp[x+around[0]][y+around[1]]=1;
                        }
                    
                    }
                }
            }
        }

        for (int i=0; i<tmp.length;i++){
            for (int j=0;j<tmp[0].length;j++){
                if(tmp[i][j]==0){
                    sum+=1;
                }
            }
        }
        
        return sum;
    }
}