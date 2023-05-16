# Um sistema de equações lineares do tipo: ax+by=c e dx+ey=f,pode ser resolvido segundo mostrado abaixo:X=ce-bf/ae-bd y=af-cd/ae-bd.Escreva um algoritmo que lê os coeficientes a,b,c,d ,e e f e calcula e mostre valores X e Y.
a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
c = int(input("Digite um valor para c: "))
d = int(input("Digite um valor para d: "))
e = int(input("Digite um valor para e: "))
f = int(input("Digite um valor para f: "))

x = (c * e) - (b * f) / (a * e) - (b * d)
y = (a * f) - (c * d) / (a * e) - (b * d)

print('O valor de x é igual a {0} e o valor de y é igual a {1}'.format(x, y))
