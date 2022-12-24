def quick_sort(arr: list):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left_arr, equal_arr, right_arr = [], [], []
    for num in arr:
        if num < pivot:
            left_arr.append(num)
        elif num > pivot:
            right_arr.append(num)
        else:
            equal_arr.append(num)  # pivot
    return quick_sort(left_arr)+equal_arr+quick_sort(right_arr)


def quick_sort2(arr: list):
    if len(arr) <= 1:
        return arr
    pivot, tail = arr[0], arr[1:]
    left_arr = [num for num in tail if num <= pivot]
    right_arr = [num for num in tail if num > pivot]

    return quick_sort(left_arr)+[pivot]+quick_sort(right_arr)


quick_sort([4, 3, 2, 5, 6, 5, 9])
print(
    "🐍 File: Sort/Quick_sort.py | Line: 29 | undefined ~ quick_sort([4, 3, 2, 5, 6, 5, 9])", quick_sort([4, 3, 2, 5, 6, 5, 9]))
quick_sort2([4, 3, 2, 5, 6, 5, 9])
print(
    "🐍 File: Sort/Quick_sort.py | Line: 32 | undefined ~ quick_sort2([4, 3, 2, 5, 6, 5, 9])", quick_sort2([4, 3, 2, 5, 6, 5, 9]))
