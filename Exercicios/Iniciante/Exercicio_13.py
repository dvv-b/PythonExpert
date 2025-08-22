#13. Solicite a quantidade de dias trabalhados e calcule o salário (considerando R$100/dia).

dias_trabalhados = int(input('Quantos dias você trabalha por mês?: '))
diaria = 100
salario = dias_trabalhados * diaria

print(f'O seu salário será de R${salario:.2f}')