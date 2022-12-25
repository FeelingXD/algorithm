def sequential_search(n, target, array):
    for i in range(int(n)):
        if array[i] == target:
            return i+1  # 위치반환 인덱스+1
    return f'Not Found target = {target}'


n, target = input().split()
print(sequential_search(n, target, [
      'Hanul', 'Jonggu', 'Dongbin', 'Taeil', 'Sangwook']))
