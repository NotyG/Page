class City():
    def __init__(self, number):
        self.number = number
        self.metros = []
        
def dateToNum(date):
    d = int(date[:2])
    m = int(date[3:5])
    y = int(date[6:]) - 1973
    return d + m*30 + y * 365
    

def findCity(cities, number):
    for i in range(len(cities)):
        if cities[i].number == number: return i
    return 'NF'
    
n = int(input())
m = int(input())
cities = []
visitedCities = []
for i in range(m):
    string = input()
    number= int(string[:-11])
    fc = findCity(cities, number)
    if fc == 'NF':
        cities.append(City(number))
        cities[-1].metros.append(dateToNum(string[-10:]))
    else:
        cities[fc].metros.append(dateToNum(string[-10:]))
k = int(input())
for i in range(k):
    string = input()
    number= int(string[:-11])
    fc = findCity(visitedCities, number)
    if fc == 'NF':
        visitedCities.append(City(number))
        visitedCities[-1].metros.append(dateToNum(string[-10:]))
    else:
        visitedCities[fc].metros.append(dateToNum(string[-10:]))
globalCount = 0
for visitedCity in visitedCities:
    city = cities[findCity(cities, visitedCity.number)]
    i = 0
    j = 0
    count = 0
    # print(type(visitedCity), type(city))
    for i in range(i, len(city.metros)):
        for j in range(j, len(visitedCity.metros)):
            if visitedCity.metros[j] >= city.metros[i]:
                count+=1
                j+=1
                break
    globalCount += count
print(globalCount)
