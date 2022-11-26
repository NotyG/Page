x, k = map(int, input().split())
n = int(input())
costs = list(map(int, input().split()))
costs.sort()
closestToK = 0
sums = {closestToK}
for cost in costs:
    newSums = set()
    for sum1 in sums:
        newSum = sum1 + cost
        if newSum <= k:
            newSums.add(newSum)
            if newSum > closestToK:
                closestToK = newSum
    sums = sums | newSums
    
ans = -1
ans = max(ans , x - (sum(costs) -  closestToK))
print(ans)
