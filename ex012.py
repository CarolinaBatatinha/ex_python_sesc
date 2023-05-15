# Desenvolva um algoritmo para calcular o montante resultante de um capital aplicado a juros compostos. Você deve pedir o capital (C), a taxa de juros (I) e o tempo (N). Com essas variáveis, você deve calcular o montante (M) pela fórmula:
# M < - C * (1+(I/100)) ^N
import math

capital = float(input("Qual o capital?:  "))
txJuros = float(input("Qual a taxa de juros?: "))
tempo = float(input("Você quer pagar em quanto tempo?: "))

montante = capital * math.pow((1 + (txJuros / 100)), tempo)

print('O montante resultante é de R${0:.2f}.'.format(montante))
