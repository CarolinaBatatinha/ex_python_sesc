# Durante uma viagem a Inglaterra você foi obrigado a comprar um termômetro, e verificou que este estava marcando a temperatura em Fahrenheit. Faça um algoritmo para calcular a conversão de graus Celcius para Fahrenheit.
tempFahr = float(input('Digite a temperatura em graus Fahrenheit: '))
tempCelsius = (tempFahr - 32)/1.8

print ('A temperatura é de {0}° C.'.format(tempCelsius))