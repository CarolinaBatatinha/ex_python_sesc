# Desenvolva um algoritmo que:
# • Peça o ano de nascimento.
# • Calcule a idade em dias.
# • Mostre a idade calculada.
import datetime

anoAtual = datetime.datetime.now().year
anoNasc = int(input('Em que ano você nasceu?: '))
idade = anoAtual - anoNasc
idadeEmDias = idade * 365

print('Você nasceu em {0}. Em {1} você terá {2} anos, que equivale a {3} dias vividos.'.format(anoNasc, anoAtual, idade, idadeEmDias))

