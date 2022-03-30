from utils import octal, convert, hexadecimal

from_type = ''
from_types = ['decimal', 'octal', 'binário']
while not (from_type in from_types):
    from_type = input('Converter de decimal, octal ou de binário? ').lower().strip()

num = ''
while not num.isdigit():
    num = input(f'Insira o número {from_type}: ').replace(' ', '')

to = ''
to_type = ['decimal', 'octal', 'hexadecimal', 'binário']
to_type.remove(from_type)
while not (to in to_type):
    to = input(f'Converter para {to_type[0]}, {to_type[1]} ou para {to_type[2]}: ').lower().strip()

if from_type == 'binário':
    if to == 'octal':
        print(f'O número binário {num} é equivalente ao octal {octal(num)}')
    elif to == 'decimal':
        print(f'O número binário {num} é equivalente ao decimal {convert(num)}')
    else:
        print(f'O número binário {num} é equivalente ao hexadecimal {hexadecimal(num)}')
elif from_type == 'octal':
    # To do
    print('Função não definida!')
elif from_type == 'decimal':
    # To do
    print('Função não definida!')
else:
    # hexadecimal
    print('Função não definida!')
