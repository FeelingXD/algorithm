#체스판 위의 룩 배치
import sys
input =sys.stdin.readline

def solution():
    test_case = int(input())

    BOARD_SIZE= 8
    ROOK="O"

    for i in range(test_case):
        board = []
        for j in range(8):
            board.append(list(map(str,input())))
        
        check_r = True
        for k in range(BOARD_SIZE):
            if board[k].count(ROOK) != 1: #가로줄 당 하나씩 있지 않으면
                check_r = False
        
        check_c = True
        if check_r == True:
            for y in range(BOARD_SIZE):
                count = 0
                for x in range(BOARD_SIZE):
                    if board[x][y] == "O":
                        count += 1
                if count != 1:
                    check_c = False
        print(f'#{i+1} yes' if check_c and check_r else f'#{i+1} no' )
                
               
if __name__== "__main__":
    solution()