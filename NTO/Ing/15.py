class Tree():
    def __init__(self, main):
        self.main = main
        self.conf = set()
    def append(self, a):
        self.conf.add(a)

def findTreeOf(trees, main):
    for i in range(len(trees)):
        if trees[i].main == main:
            return i
    return 'NF'
    

N, M = map(int, input().split())
types = {i for i in range(1, N+1)}
trees = []
for i in range(M):
    main, a = map(int, input().split())
    index = findTreeOf(trees, main)
    if index == 'NF':
        trees.append(Tree(main))
        trees[-1].append(a)
    else:
        trees[index].append(a)
    index = findTreeOf(trees, a)
    if index == 'NF':
        trees.append(Tree(a))
        trees[-1].append(main)
    else:
        trees[index].append(main)
firstDay = set()
secondDay = set()
ans = 'Yes'
for i in range(len(trees)):
    if firstDay.isdisjoint(trees[i].conf):
        firstDay.add(trees[i].main)
    elif secondDay.isdisjoint(trees[i].conf):
        secondDay.add(trees[i].main)
    else:
        ans = 'No'
print(ans)
