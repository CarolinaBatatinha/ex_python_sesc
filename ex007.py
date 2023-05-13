# Desenvolva um programa para resolver as seguintes equações:
# • x*y
# • x2+y (para fazer x2, use: x*x ou x^2)
# • (4/r) * (w+r)
import math

x = int(input("Digite um valor para x: "))
y = int(input("Digite um valor para y: "))
w = int(input("Digite um valor para w: "))
r = int(input("Digite um valor para r: "))

primEq = x * y
segEq = math.pow(x, 2) + y
terEq = round((4 / r) * (w + r), 2) #COMO LIMITAR O NÚMERO DE CASAS DECIMAIS

print('x * y = {0} x {1} = {2}'.format(x, y, primEq))
print('x² + y = {0}² + {1} = {2}'.format(x, y, segEq))
print('(4 / r) x (w + r) = (4 / {0}) x ({1} + {0}) = {2}'.format(r, w, terEq))
