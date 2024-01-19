#진주로 가자! (Easy)
import sys
import heapq
from collections import defaultdict
input =sys.stdin.readline
def input_process(line):
    dest,fee=line.split()
    return (dest,int(fee))

def solution():
    dic=defaultdict(int)
    heap=[]
    for _ in range(case:=int(input())):
        dest,fee=input_process(input().strip())
        dic[dest]=fee
        heapq.heappush(heap,fee)
    while heap and heap[0]<=dic['jinju']:
        heapq.heappop(heap)
    print(dic['jinju'])
    print(len(heap))
    
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass