#Faça um algoritmo para ler dois números e realizar as operações aritméticas: adição, subtração e multiplicação. Para cada operação o resultado deve ser impresso no vídeo.
num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
print('Soma: {0} + {1} = {2}'.format(num1, num2, soma))
print('Subtração: {0} - {1} = {2}'.format(num1, num2, subtracao))
print('Multiplicação: {0} x {1} = {2}'.format(num1, num2,multiplicacao))