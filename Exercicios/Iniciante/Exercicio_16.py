# 16. Solicite 3 notas de um aluno e mostre a média final.

nota_1 = float(input('informe sua primeira nota: '))
nota_2 = float(input('informe sua segunda nota: '))
nota_3 = float(input('informe sua terceira nota: '))
media = (nota_1 + nota_2 + nota_3) / 3

print(f'A média das notas é {media:.2f}')