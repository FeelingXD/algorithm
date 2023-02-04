def solution(n, i, j):
    def recursion(count, n, i, j):
        if n == 2:
            return count + 2 + i + (-1)**(i+1)*j

        m = n // 2
        if i < m and j >= m:
            return recursion(count, m, i, j-m)
        elif i < m and j < m:
            return recursion(count + m**2, m, i, j)
        elif i >= m and j < m:
            return recursion(count + 2 * m**2, m, i - m, j)
        else:
            return recursion(count + 3 * m**2, m, i - m, j - m)

    return recursion(0, n, i, j)


print("🐍 File: review/#test.py | Line: 20 | undefined ~ ",
      solution(8, 1, 3))
