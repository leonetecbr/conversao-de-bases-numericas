from utils import octal, convert, hexadecimal

num = ''
while not num.isdigit():
    num = input('Insira o número binário: ').replace(' ', '')

to = ''
while not (to == 'decimal' or to == 'octal' or to == 'hexadecimal'):
    to = input('Converter para decimal, octal ou para hexadecimal? ').lower().strip()


if to == 'octal':
    print(f'O número binário {num} é equivalente ao octal {octal(num)}')
elif to == 'decimal':
    print(f'O número binário {num} é equivalente ao decimal {convert(num)}')
else:
    print(f'O número binário {num} é equivalente ao hexadecimal {hexadecimal(num)}')
