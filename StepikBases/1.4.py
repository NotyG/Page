n, k = map(int, input().split())
a= list(map(int, input().split()))
pref = [0]*(n+1)
for i in range(1, n+1):
    pref[i] += pref[i-1] + a[i-1]
i = 1
j = 1
count = 0
while j != n+1:
    #print(j)
    if pref[j]-pref[i-1] >= k:
        count += n-j+1
        i += 1
    else:
        j+=1

print(count)