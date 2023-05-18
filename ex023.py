# O proprietário de um restaurante deseja informatizar o seu estabelecimento, para tanto você foi contratado com o seguinte propósito. Elabore um algoritmo que leia o número da mesa e qual a quantidade dos itens consumidos de um determinado cardápio, para que se possa saber o valor total desta mesa (conta), o algoritmo deverá prever a entrada do número de pessoas existentes na mesa para que seja feita a divisão da mesma, entre os seus ocupantes.
# Cardápio:
# Refrigerante 1.20
# Cerveja 1.50
# Almoço 6.30
# Porção 4.50
# Lanche 4.00

mesa = int(input('Qual o número da mesa a ser atendida?: '))
clientes = int(input('Quantos consumidores na mesa?: '))

refri = float(1.20)
cerveja = float(1.50)
almoco = float(6.30)
porcao = float(4.50)
lanche = float(4.00)

qtRefri = int(input('Quantidade de refrigerante: '))
qtCerveja = int(input('Quantidade de cerveja: '))
qtAlmoco = int(input('Quantidade de almoço: '))
qtPorcao = int(input('Quantidade de porções: '))
qtLanche = int(input('Quantidade de lanche: '))

valorConsumido = (refri * qtRefri) + (cerveja * qtCerveja) + (almoco * qtAlmoco) + (porcao + qtPorcao) + (lanche * qtLanche)

valorDividido = valorConsumido / clientes

print('A mesa {0} tem {1} clientes. O valor total é de R$ {2:.2f} e, dividido entre todos, cada um paga R$ {3:.2f}'.format(mesa, clientes, valorConsumido, valorDividido))




