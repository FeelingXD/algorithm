# 재귀 구현

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


# 반복문 구현

def binary_search_loop(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return (f'not found target : {target} in array: {arr}')
