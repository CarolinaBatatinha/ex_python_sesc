# Faca um algoritmo que:
# • Peca o valor a prazo do produto
# • Peca a alíquota do desconto
# • Calcule o preço a vista do produto
aPrazo = float(input('Qual o valor do produto a prazo?: '))
desconto = float(input('Qual o desconto dado?: '))

aVista = round(aPrazo - (aPrazo * (desconto/100)), 2)

print('À vista, o preço cai pra R${0}.'.format(aVista))