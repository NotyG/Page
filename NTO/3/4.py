# class Cell():
    # def __init__(self):
        # self.Yn = 0
        # self.An = 0
        # self.k = 0
n, m, k = map(int, input().split())
ts = list(map(int, input().split()))
tAns = [0]*(m*n+1)
# table = [[0]*m for i in range(n)]
AnNum = 1
YnNum = None
dir = None
#print(table)
xl, xr, yu, yd = 0, m - 1, 0, n - 1
x = xl -1
y = yd
for i in range(n):
    for j in range(m):   
        if x == xr and y == yd + 1 and dir != 'u':
            dir = 'u'
            xr -= 1
        if x == xl and y == yu - 1 and dir != 'd':
            dir = 'd'
            xl += 1
        if y == yu and x == xr + 1 and dir != 'l':
            dir = 'l'
            yu += 1
        if y == yd and x == xl - 1 and dir != 'r':
            dir = 'r'
            yd -= 1
            
        if dir == 'r':
            x += 1
                
        if dir == 'l':
            x -= 1
        if dir == 'u':
            y -= 1
        if dir == 'd':
            y += 1
        
        if x % 2 == 1:
            YnNum = n*x + y + 1
        else:
            YnNum = n*(x+1)-y
        # print(y, x, dir, AnNum, YnNum, end = '\n')
        # table[y][x] = max(YnNum, AnNum)
        
        # table[y][x] =Cell()
        # table[y][x].An = AnNum
        # table[y][x].Yn = YnNum
        # table[y][x].k = max(AnNum, YnNum)
        # print(table[y][x].An)
        
        tAns[max(AnNum, YnNum)] += 1
        AnNum += 1
# print(*tAns)
tPref = [0]*(m*n+1)
for i in range(1, m*n+1):
    tPref[i] += tPref[i-1] + tAns[i]
# print(*tPref)
# print('ans')
for t in ts:
    print(tPref[t], end = ' ')  

# print('logs')
# for line in table:
    # for cell in line:
        # print(cell.An, end = ' ')
    # print()
# print()
# for line in table:
    # for cell in line:
        # print(cell.Yn, end = ' ')
    # print()
# print()
# for line in table:
    # for cell in line:
        # print(cell.k, end = ' ')
    # print()
