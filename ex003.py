#Faça um algoritmo para ler dois números e fazer a troca dos valores digitados pelo usuário. Após a troca, imprima os novos valores obtidos
numA = int(input('Digite um número: '))
numB = int(input('Digite outro número: '))

troca = numA
numA = numB
numB = troca

print('A primeira variável agora vale {0} e a segunda variável vale {1}.'.format(numA, numB))