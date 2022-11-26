n, k = map(int, input().split())
if k != 0:
    k = k % 4
    if k == 0: k = 4
print(n**k % 10)
