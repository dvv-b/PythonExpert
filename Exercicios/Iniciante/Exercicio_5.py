#5. Solicite ao usuário que digite sua idade e diga se ele já pode dirigir (18 anos ou mais).

idade_minima = 18

usuario = int(input('Qual a sua idade?: '))

if usuario >= idade_minima:
    print('Você é maior de idade e pode dirigir')

else:
    print('Você é menor de idade e não pode dirigir')