#A Empresa ABC produz 3 tipos de peças mecânicas: parafusos, porcas e arruelas. Sabe-se que é dado desconto de: 10% por porca vendida, 20% por Arruelas vendidas, 30% por parafusos vendidos. Dados de Entrada: nome do cliente; preço unitário da porca, arruela, parafuso; quantidade de porcas, arruelas e parafusos solicitados pelo cliente. Dados de Saída: nome do cliente; número de porcas, arruelas e parafusos comprados; total pago pelas porcas, arruelas e parafusos; total de desconto dado ao cliente; total a ser pago pelo cliente.

# Inputs
cliente = input('Nome do cliente: ')
precoPorca = float(input('Preço unitário da porca: '))
precoArruela = float(input('Preço unitário da arruela: '))
precoParafuso = float(input('Preço unitário do parafuso: '))
quantPorcas = int(input('Quantidade de porcas: '))
quantArruelas = int(input('Quantidade de arruelas: '))
quantParafusos = int(input('Quantidade de parafusos: '))

totalPorcas = quantPorcas * precoPorca
totalArruelas = quantArruelas * precoArruela
totalParafusos = quantParafusos * precoParafuso

descontoPorcas = totalPorcas * 0.1
descontoArruelas = totalArruelas * 0.2
descontoParafusos = totalParafusos * 0.3

totalDesconto = descontoPorcas + descontoArruelas + descontoParafusos

totalPago = totalPorcas + totalArruelas + totalParafusos - totalDesconto

print('========================================================')
print('Nome do cliente:', cliente)
print('Número de porcas compradas:', quantPorcas)
print('Número de arruelas compradas:', quantArruelas)
print('Número de parafusos comprados:', quantParafusos)
print('Total pago pelas porcas:', totalPorcas)
print('Total pago pelas arruelas:', totalArruelas)
print('Total pago pelos parafusos:', totalParafusos)
print('Total de desconto dado ao cliente:', totalDesconto)
print('Total a ser pago pelo cliente:', totalPago)

