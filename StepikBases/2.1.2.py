class Point():
    def __init__(self, x, type):
        self.x = x
        self.type = type
    def __lt__(self, a):
        if self.x < a.x:
            return True
        elif self.x == a.x:
            if self.type > a.type:
                return True
        return False
n = int(input())
points = []
for i in range(n):
    x1, x2 = map(int,input().split())
    points.append(Point(x1, 1))
    points.append(Point(x2, -1))
points.sort()
state = 0 
maxState = -1
maxX = None
overLaps = 0
for point in points:
    print(point.x, end = ' ')
print()
for point in points:
    print(point.type, end = ' ')
print()
for i in range(n*2):
    
    if i >= 1:
        if points[i-1].x == points[i].x: 
            if points[i-1].type == -1:
                overLaps += 1
        else:
            overLaps = 0
    state += points[i].type
    # print(i, points[i].x, points[i].type, state, overLaps)
    if state + overLaps> maxState:
        maxState = state + overLaps
        maxX = points[i].x
print(maxX, maxState)