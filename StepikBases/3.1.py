n = int(input())
matrix = []
for i in range(n):
    line = list(map(int, input().split()))
    k = line[0]
    arr = [0] * n
    for i in range(1, k+1):
        arr[line[i]-1] = 1
    matrix.append(arr)
for line in matrix:
    print(*line)