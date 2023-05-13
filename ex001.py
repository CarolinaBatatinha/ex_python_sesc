# Faça um algoritmo para ler um número, somá-lo com o valor 10 e mostrar a média entre o número lido e o valor 10.
fixo = 10
num = int(input("Digite um número inteiro: "))
soma = num + fixo
media = soma / 2

print("A soma é igual a {0} e a média dos valores é igual a {1}.".format(soma, media))
