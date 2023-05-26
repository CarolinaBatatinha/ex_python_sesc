# Faça um algoritmo para ler quatro notas e imprimir a média ponderada dessas notas. Considere que os pesos das são: 1, 2, 3 e 4, respectivamente.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

peso1 = int(1)
peso2 = int(2)
peso3 = int(3)
peso4 = int(4)

media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3) + (nota4 * peso4))/ (peso1 + peso2 + peso3 + peso4)

print(f'A media ponderada dessas notas é {media}.')
