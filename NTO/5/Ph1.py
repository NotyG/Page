from math import pi
d1 = 0.15
d2 = 0.25
h = 0.26
p = 1020
h1 = (h * d1) / (d2 - d1)
h2 = h1 + h
v = (1 / 12) * pi * (d2**2 * h2 - d1**2 * h1)
print(p * v)