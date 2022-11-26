n = int(input())
a = [0] + list(map(int, input().split()))
s = 0
l = 0
r = 0
zeroPoint = 0
maxS = -1
for i in range(1, n+1):
    s += a[i]
    if s < 0:
        zeroPoint = i
        s = 0
    if s > maxS:
        l = zeroPoint + 1
        r = i
        maxS = s
print(l, r, maxS)