#------------------------------------------
# Programa para calcular las raices de una ecuación de primer grado con una variable



#------------------------------------------
# Programa para calcular las raices de una ecuación de segundo grado con una variable

import cmath

a = 1
b = 0
c = -4

x_1 = 0
x_2 = 0

x_1 = (-b + cmath.sqrt(b**2 - 4*a*c))/2
x_2 = (-b - cmath.sqrt(b**2 - 4*a*c))/2

print(x_1, '\n')

print(x_2)