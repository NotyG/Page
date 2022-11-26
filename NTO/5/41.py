# file = open('4Test.out')
# fileOut = open('41.out', 'w')
string = input()
# string = file.read()
# string = '.*..*..*.**...**'
for i in range(len(string)):
    if string[i] == '.':
        string = string[i:] + string[:i]
        break
count = 0
l = 0
maxL, maxR = 0, 0
maxLength = 0
length = 0
countOfPieces = 0
for i in range(len(string)):
    if string[i] == '*':
        countOfPieces += 1
        if length == 0:
            l = i
        length += 1
    if string[i] == '.':
        length = 0
    if length > maxLength:
        maxLength = length
        maxL = l
        maxR = i
# print(*string)
string = string[(maxR+1):] + string[:(maxR+1)]
# stringF = list(string)
maxL = len(string) - maxLength
# i = -1
# r = maxL
#lAdded = 0
#rAdded=0
# print(*string)
# print(maxLength, countOfPieces, i, r, maxL)
length = maxLength
while maxLength != countOfPieces:
    countOfPiecesBefore = 0
    for i in range(0, maxL):
        if string[i] == '*':
            countOfPiecesBefore += 1
        # if i % 1000 == 0: print(i)
        if string[i] == '*':
            # leftOnTheWay = countOfPiecesBefore - 1 - lAdded - rAdded
            leftOnTheWay = countOfPiecesBefore - 1
            rightOnTheWay = countOfPieces - countOfPiecesBefore - length  #string[(i+1):].count('*') - (maxLength - lAdded) #(maxLength - lAdded) = rAdded
            #if leftOnTheWay > rightOnTheWay: break
            if i - leftOnTheWay <= abs(i - maxL)-1 - rightOnTheWay: #and leftOnTheWay == 0:
                count += i - leftOnTheWay #abs(i - i) -1 - leftOnTheWay
                # l += 1
              # lAdded += 1
              # stringF[i] = '.'
                # stringF[i] = '*'
                maxLength += 1
            if abs(i - maxL)-1 - rightOnTheWay < i - leftOnTheWay: #and rightOnTheWay == 0:
                count += abs(i - maxL)-1 - rightOnTheWay
                # r -= 1
                # rAdded +=1
                # stringF[i] = '.'
                # stringF[r] = '*'
                maxLength += 1
            # print(i, count ,lAdded, rAdded, countOfPiecesBefore, leftOnTheWay, rightOnTheWay, *stringF)
print(count)