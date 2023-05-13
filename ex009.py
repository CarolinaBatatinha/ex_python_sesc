#Desenvolva um algoritmo que:
#• Peca o valor do produto
#• Peca a valor da aliquota
#• Calcule o valor em reais da porcentagem informada.

preco = float(input('Qual o valor do produto?: '))
desconto = float(input('Qual o desconto dado?: '))

valorDesconto = round(preco * (desconto/100), 2)

print('O desconto dado é de R${0}.'.format(valorDesconto))