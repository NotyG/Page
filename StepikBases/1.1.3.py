n = int(input())
arr = list(map(int, input().split()))
minus_sum = -1
sum = 0
ans = arr[0]
l = 0
r = 0
for i in range(n):
    sum += arr[i]
   # print(i, sum, ans, l, r)
    if sum > ans:
        ans = sum
        l = minus_sum + 1
        r = i
    if sum < 0:
        minus_sum = i
        sum = 0 
print(l+1, r+1, ans)
     