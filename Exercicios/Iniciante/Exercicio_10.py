#10. Peça o salário de um funcionário e calcule um aumento de 10%.

salario = float(input('Qual é o seu salário?: '))
aumento = 0.1

salario_aumentado = salario * aumento + salario

print(f'Seu novo salário após acrescimo é de R${salario_aumentado}')
