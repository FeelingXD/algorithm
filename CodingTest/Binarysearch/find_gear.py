# 부품 찾기
import sys

# 재귀


def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)


n = int(sys.stdin.readline())
arr_n = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr_m = list(map(int, sys.stdin.readline().split()))

# for loop
for value in arr_m:
    if binary_search(arr_n, value, 0, len(arr_m)) != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 계수정렬

count_arr = [0] * (max(arr_n) + 1)

for i in arr_n:
    count_arr[i] = 1
print('')
for i in arr_m:
    if count_arr[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
