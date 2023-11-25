#A 와 B
import sys
input = sys.stdin.readline
def greedy(T,S):
    # T->S가 될수있는지 반대로탐색
    while len(T)>=len(S):
        if T==S:
            return 1
        elif T[-1]=='B':
            # T의 마지막값이 'B' 일때 뒤집는과정과 함께하기에 마지막문자를 제외하고 뒤집힌값을 T로설정한다.
            T=T[:len(T)-1][::-1]
        elif T[-1]=='A':
            # 마지막 값이 'A'일때는 단순히 마지막값을제외해준다.
            T=T[:len(T)-1]
    else:
        return 0
    
    pass

def solution():
    '''
    S 와 T를 입력받고 다음 두가지 연산을통해 S에서 T가 될수있는지 확인
    - 문자열 뒤에 A를 추가하기
    - 문자열을 뒤집고 B를 추가하기
    '''
    S= input().strip()
    T= input().strip()
    print(greedy(T,S))
    pass

if __name__=="__main__":
    solution()
    pass