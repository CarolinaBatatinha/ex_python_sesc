# 16. Você foi encarregado de desenvolver o modulo de cálculo da folha de pagamento de uma empresa. O funcionamento do programa deve ser o seguinte:
# • Peca o nome do empregado.
# • Peca o salário bruto
# • Peca o valor do Imposto de Renda em reais que será descontado
# • Peca o valor da previdencia (INSS) em reais que será descontado.
# • Calcule o valor do salário liquido do empregado
# • Informe o salário liquido com a seguinte frase:
# Fulano, seu salário liquido é: ......

nomeFuncionario = input("Digite seu nome: ")
salarioBruto = float(input("Digite seu salário bruto em reais(R$): "))
valorIR = float(input("Digite o valor do Imposto de Renda a ser descontado em reais(R$): "))
valorINSS = float(input("Digite o valor da previdência a ser descontado em reais(R$): "))

salarioLiquido = salarioBruto - valorIR - valorINSS
print("{0}, seu salário líquido é de R$ {1:.2f}.".format(nomeFuncionario, salarioLiquido))
