# Faça um programa que leia os valores A, B, C, D, E, F e encontre o valor de X

# X = (a + (b/c) / d - 2 * (e/f)) + 4a

A = float(input("Digite um valor para A: "))
B = float(input("Digite um valor para B: "))
C = float(input("Digite um valor para C: "))
D = float(input("Digite um valor para D: "))
E = float(input("Digite um valor para E: "))
F = float(input("Digite um valor para F: "))

X = A + (B / C) / D - 2 * (E / F) + 4 * A

print('O valor da expressão é {0:.1f}.'.format(X))