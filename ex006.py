# Faça um programa para calcular o cubo de um número informado pelo usuário. Em seguida, faça a diferença desse resultado com o número lido.

import math

num = int(input('Digite um número: '))
cubo = math.pow(num, 3)
subtracao = cubo - num

print('A raiz cúbica de {0} é igual a {1}.'.format(num, cubo))
print('A diferença entre {0} e {1} é igual a {2}.'.format(cubo, num, subtracao))
