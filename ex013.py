# Escreva um algoritmo que solicite ao usuário a altura e o raio de um cilindro circular, e imprima o volume do cilindro. O volume do cilindro circular é calculado pela seguinte formula: volume = 3.141592 * raio * raio * altura.
import math

altura = float(input("Qual a altura do cilindro em cm?: "))
raio = float(input("Qual o raio do cilindro em cm?: "))

volume = round((math.pi * math.pow(raio, 2) * altura), 2)

print("O volume do cilindro é de {0}cm³.".format(volume))
