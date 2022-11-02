n, m = map(int,input().split())
s = []
for i in range(1,n+1):
    s.append(' '.join(map(str,range((i-1)*m+1, i*m+1))))
print('\n'.join(s))
