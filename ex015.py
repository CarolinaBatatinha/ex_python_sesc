# A importância de R$ 780.000,00 será dividida entre os três primeiros colocados de um concurso, em partes diretamente proporcional aos pontos conseguidos por eles. Construa um programa que leia o numero de pontos dos três primeiros colocados e imprima a importância que caberá a cada um deles.

parte = int(780000/ 6)

primeiro = round(3 * parte, 2)
segundo = round(2 * parte, 2)
terceiro = round(1 * parte, 2)

print('O primeiro colocado levará R${0}, o segundo colocado levará R${1} e o terceiro colocado levará R${2}.'.format(primeiro, segundo, terceiro))
