string = input()
arrows = []
arrow = ''
arrowType = ''
MainArrowType = ''
for l in string:
    if l == '-':
        if arrowType == '>':
            arrows.append(arrow)
            arrow = ''
        arrowType = '-'
        arrow += l
    if l == '<':
        if arrowType == '>':
            arrows.append(arrow)
            arrow = ''
            lastArrowType = '>'
        if arrowType == '-':
            arrows.append(arrow)
            arrow = ''
        MainArrowType = '<'
        lastArrowType = '<'
        arrowType = '<'
        arrow += l
    if l == '>':
        if MainArrowType == '<':
            arrows.append(arrow[:-1])
            arrow = arrow[-1]
        MainArrowType = '>'
        arrowType = '>'
        arrow += l
arrows.append(arrow)
print(*arrows, sep='\n')