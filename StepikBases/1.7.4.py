n = int(input())
a = [0] + list(map(int, input().split()))
q = int(input())
t = [0]
for _ in range(q):
    t.append(int(input()))
m = [0]*(q+1)
v = [0]*(q+1)
aPref = a.copy()
for i in range(1, n+1):
    aPref[i] += aPref[i-1] 
# print('a', *aPref)
for i in range(1, q+1):
    if t[i] == 1:
        m[i] += 1
    if t[i] == 2:
        v[i] += 1
    m[i] += m[i-1]
    v[i] += v[i-1]
    # print(i, t[i], '\n', *m, '\n', *v)
    if t[i] == 3:
        print(aPref[v[i]]- aPref[m[i]])
        