#  Desenvolva um programa para cálculo de salário liquido de um funcionário O programa deve:
# • Pedir o salário bruto do funcionário
# • Calcular o valor do IR com alíquota de 10%
# • Calcular o valor do INSS com alíquota de 5%
# • Calcular o salário liquido do funcionário

salBruto = float(input('Digite seu salário bruto em reais: '))
descontoIR = float(salBruto * 0.1)
descontoINSS = float(salBruto * 0.05)
salLiquido = salBruto - descontoINSS - descontoIR

print('Depois de tanto desconto, o salário líquido fica em R${0}.'.format(salLiquido))
