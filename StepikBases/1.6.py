n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
for i in range(1, n+1):
    print(i , end = ' ')
print('\n', end = '')
l = 1
r = 1
j = 1
i = 1
jLast = 0
length = 0
numsSet = set()
numsSet.add(a[1])
nums = [a[1]]
# print(*a)
for i in range(i, n+1):
    for j in range(j, n+1):
        if i == j:
            continue
        if j != jLast:
            jLast = j
            nums.append(a[j])
        if not( a[j] in numsSet):
            numsSet.add(a[j])
        if len(numsSet) > k:
            break
        print(i, j, end = '  ')
        if len(nums) >= r- l + 1 and numsSet == set(nums):
            # length = r - l + 1
            l = i
            r = j
            print(True, end = ' ')
        print(nums,l, r, numsSet)
    if a[i]in numsSet:
        numsSet.remove(a[i])
    nums.pop(0)
print(l, r)
        