from math import floor

hexa = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}


def convert(number):
    """
    Converte o número binário em octal ou decimal
    :param number:string
    :return :integer
    """
    size = len(number)
    count = 0
    result = 0
    while count < size:
        result += int(number[size - count - 1]) * (2 ** count)
        count += 1

    return result


def octal(number):
    """
    Converte números binários em octal
    :param number:integer
    :return :integer
    """
    length = len(number)
    result = []
    i = 0

    while i < length:
        start = length - i
        if start >= 3:
            start -= 3
        else:
            start = 0
        end = length - i
        result.append(str(convert(number[start:end])))
        i += 3

    return int(''.join(reversed(result)))


def hexadecimal(number):
    """
    Converte números binários em hexadecimal
    :param number:string
    :return :string
    """
    length = len(number)
    result = []
    i = 0
    array = ['A', 'B', 'C', 'D', 'E', 'F']

    while i < length:
        start = length - i
        if start >= 4:
            start -= 4
        else:
            start = 0
        end = length - i
        num = convert(number[start:end])
        if num > 9:
            num = array[num - 10]
        result.append(str(num))
        i += 4

    num_hex = ''.join(reversed(result))
    while num_hex[0] == '0':
        num_hex = num_hex[1:]

    return num_hex


def binario(num):
    """
    Converte decimal em binário
    :param num:integer
    :return :string
    """
    new_binary = []
    num = int(num)

    while num >= 2:
        new_binary.append(str(num % 2))
        num = floor(num / 2)

    new_binary = str(num) + ''.join(reversed(new_binary))

    return new_binary


def binario_size(num, tamanho=4):
    """
    Converte octal e hexadecimal em binário
    :param num:string
    :param tamanho:integer
    :return :string
    """
    binary = ''
    for n in num:
        if not n.isdigit():
            n = hexa[n]
        new_binary = binario(n)

        while len(new_binary) < tamanho:
            new_binary = '0' + new_binary

        binary += new_binary

    return binary
