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
