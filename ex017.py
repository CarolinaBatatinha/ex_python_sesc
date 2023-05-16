# Você foi contratado por uma empresa de construção para fazer um programa que calcule o salário liquido dos operários no fim de cada mês, sabe-se que cada operário recebe R$ 3,00 por cada hora trabalhada, e que se desconta 8% do salário bruto para INSS.

horasTrabalhadas = float(input("Por quantas horas você trabalhou esse mês?: "))
salarioBruto = 3 * horasTrabalhadas
valorINSS = salarioBruto * 0.08
salarioLiquido = salarioBruto - valorINSS

print("Seu salário líquido é de R$ {0:.2f}.".format(salarioLiquido))
