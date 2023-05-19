# Você foi contratado por uma loja de eletrônicos para fazer um algoritmo que calcule a conversão de dólares para real, sabe-se que o  programa deverá ler a cotação do Dólar do dia e o valor a ser convertido.

cotacaoDolar = float(input("Digite a cotação do dólar (US$) hoje em reais (R$): "))
valorEmReais = float(input("Digite quantos reais (R$) você tem: "))
resultado = valorEmReais / cotacaoDolar

print("Hoje, com R$ {0:.2f}, você pode comprar US$ {1:.2f}.".format(valorEmReais, resultado))
