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
