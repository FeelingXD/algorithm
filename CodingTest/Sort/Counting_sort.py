# 계수정렬

# 조건
# 원소 모두가 양수일것

def count_sort(arr: list):
    arr_count = [0]*len(arr)
    for num in arr:
        arr_count[num] += 1
    return arr_count


def print_count_sort(arr: list):
    for i in range(len(arr)):  # 0 1 2 3 index
        print((str(i)+' ')*arr[i], end='')


arr = [0, 0, 1, 0, 1, 2, 3, 4, 5]
print_count_sort(count_sort(arr))
