from utils import octal, convert

num = input('Insira o número binário: ').replace(' ', '')

to = ''
while not (to == 'decimal' or to == 'octal'):
    to = input('Converter para decimal ou para octal? ').lower().strip()


if to == 'octal':
    print(octal(num))
else:
    print(convert(num))