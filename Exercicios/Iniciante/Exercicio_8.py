# 8. Solicite ao usuário que digite um valor em metros e converta para centímetros e milímetros.

usuario = float(input('Digite quantos metros tem a parede do seu quarto: '))

centimetros = usuario * 100
milimetro = usuario * 1000

print(f'''O valor da parede em centimetros é: {centimetros}cm 
O valor da parede em milimetros é: {milimetro}mm''')

