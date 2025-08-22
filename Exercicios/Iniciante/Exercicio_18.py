#18. Calcule o IMC de uma pessoa (peso ÷ altura²).

peso = float(input('Qual é o seu peso?: '))
altura = float(input('Qual a sua altura:?'))
imc = peso / (altura * altura)

print(f'O seu IMC é de: {imc:.2f}')

