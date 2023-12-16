#강의실 배정
import sys
import heapq
input =sys.stdin.readline

def solution():
    lectures=[tuple(map(int,input().split())) for _ in range(int(input()))]
    lectures.sort()
    room=[lectures[0][1]] # 끝나는 시간
    for i in range(1,len(lectures)):
        if room[0]<=lectures[i][0]:
            heapq.heappop(room)
        heapq.heappush(room,lectures[i][1])
    print(len(room))
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass
