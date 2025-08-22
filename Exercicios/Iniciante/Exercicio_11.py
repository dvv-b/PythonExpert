#11. Solicite o preço de um produto e calcule o desconto de 5%.

produto = float(input('Qual é o preço do seu celular?: '))
desconto = 0.05

produto_desconto = produto - desconto * produto

print(f'O preço do celular após o desconto é de R${produto_desconto:.2f}')