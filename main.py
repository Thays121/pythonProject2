A = int(input('digite o 1º lado do triângulo:'))
B = int(input('digite o 2º lado do triângulo:'))
C = int(input('digite o 3º lado do triângulo:'))

if (A > 0 ) and (B > 0) and (C > 0):
    if (A + B > C) and (A + C > B) and (B + C > A):
    # Se  voce chegou ate aqui, e porque o triangulo e válido!
         if A != B and A != C and B != C:
             print('Triangulo escaleno!')
         else:
             if A == B and  A == C and B == C:
                 print('Triangulo equilatero!')
             else:
                 print('Triangulo isosceles!')
    else:
        print('Ao menos um dos valores não servem para formar um triangulo')

else:
    print('Ao menos um dos valores não servem para formar um triangulo')