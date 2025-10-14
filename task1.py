a = int(input())
b = int(input())
alpha = float(input())

from math import cos, sqrt, radians
alpha = radians(alpha)
c = a**2 + b**2 - 2 * a * b * cos(alpha)
c = sqrt(c)
print('Длина третьей стороны:', c)
