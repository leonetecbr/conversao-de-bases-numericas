from utils import octal, convert, hexadecimal, binario, binario_size
import re

from_type = ''
from_types = ['decimal', 'octal', 'binário', 'hexadecimal']
while not (from_type in from_types):
    from_type = input('Converter de decimal, octal, hexadecimal ou de binário? ').lower().strip()

num = ''
while not num.isdigit():
    if re.match(r'([A-F]|[0-9])+', num) and from_type == 'hexadecimal':
        break

    num = input(f'Insira o número {from_type}: ').upper().replace(' ', '')

to = ''
to_type = ['decimal', 'octal', 'hexadecimal', 'binário']
to_type.remove(from_type)
while not (to in to_type):
    to = input(f'Converter para {to_type[0]}, {to_type[1]} ou para {to_type[2]}: ').lower().strip()

result = ''
if from_type == 'binário':
    if to == 'octal':
        result = octal(num)
    elif to == 'decimal':
        result = convert(num)
    else:
        # Hexadecimal
        result = hexadecimal(num)
elif from_type == 'octal':
    if to == 'binário':
        result = binario_size(num, 3)
    elif to == 'decimal':
        result = convert(binario_size(num, 3))
    else:
        # Hexadecimal
        result = hexadecimal(binario_size(num, 3))
elif from_type == 'decimal':
    if to == 'binário':
        result = binario(num)
    elif to == 'hexadecimal':
        result = hexadecimal(binario(num))
    else:
        # Octal
        result = octal(binario(num))
else:
    if to == 'binário':
        result = binario_size(num)
    elif to == 'decimal':
        result = convert(binario_size(num))
    else:
        # Octal
        result = octal(binario_size(num))

print(f'O número {from_type} {num} é equivalente ao {to} {result}')
