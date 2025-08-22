#15. Peça o ano de nascimento do usuário e calcule sua idade.

from datetime import date

ano_nascimento = int(input('Em qual ano você nasceu?: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f'Você tem {idade} anos')