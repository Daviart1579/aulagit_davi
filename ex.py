ação = int(input('escolha uma tipo de função: 1,2,3,4:'))
n1 = int(input('digite um numero:'))
n2 = int(input('digite outro numero:'))

def soma (n1, n2):
    print(n1+n2)

def subtração (n1, n2):
    print(n1-n2)

def divisão (n1, n2):
    print(n1/n2),

def multiplicação (n1, n2):
    print(n1*n2)

if ação ==1:
    soma(n1, n2)

if ação ==2:
    subtração(n1, n2)

if ação ==3:
    divisão(n1, n2)

if ação ==4:
    multiplicação(n1, n2)
