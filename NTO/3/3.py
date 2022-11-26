n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0
sMax = 0
if n == 1:
    sMax = a[0] * b[0]/(a[0]+b[0])
if n == 2:
    for i100 in range(0, 101):
        s = 0
        for j100 in range(0, 101):
            i = i100 / 100
            j = j100 / 100
            if a[0] * i + a[1] * j == b[0] * (1-i) + b[1] * (1-j):
                s = a[0] * i + a[1] * j
                sMax = max(s, sMax)
if n == 3:
    for i100 in range(0, 101):
        s = 0
        for j100 in range(0, 101):
            for k100 in range(0, 101):
                i = i100 / 100
                j = j100 / 100
                k = k100 / 100
                if a[0] * i + a[1] * j + a[2] * k == b[0] * (1-i) + b[1] * (1-j) + b[2] * (1-k):
                    s = a[0] * i + a[1] * j + a[2] * k
                    sMax = max(s, sMax)
print(sMax)