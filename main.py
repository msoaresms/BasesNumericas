def decParaBin(decimal):
    bin = []
    while (decimal // 2 >= 1):
        bin.insert(0, decimal % 2)
        decimal = decimal // 2
    bin.insert(0, 1)
    return bin

def decParaHex(decimal):

    binParaHex = {}
    binParaHex['0000'] = '0'
    binParaHex['0001'] = '1'
    binParaHex['0010'] = '2'
    binParaHex['0011'] = '3'
    binParaHex['0100'] = '4'
    binParaHex['0101'] = '5'
    binParaHex['0110'] = '6'
    binParaHex['0111'] = '7'
    binParaHex['1000'] = '8'
    binParaHex['1001'] = '9'
    binParaHex['1010'] = 'A'
    binParaHex['1011'] = 'B'
    binParaHex['1100'] = 'C'
    binParaHex['1101'] = 'D'
    binParaHex['1110'] = 'E'
    binParaHex['1111'] = 'F'

    bin = decParaBin(decimal)
    bin4 = []
    hex = []
    while (len(bin) % 4 != 0):
        bin.insert(0, 0)

    n = 0
    m = n + 4

    while (m <= len(bin)):
        bin4.append(''.join(map(str, bin[n:m])))
        n = m
        m = n + 4

    for x in bin4:
        hex.append(binParaHex[x])

    return hex





decimal = int(input('Informe um número na base decimal: '))
print()

bin = decParaBin(decimal)
for x in bin:
    print(x, end='')
print()
hex = decParaHex(decimal)
for x in hex:
    print(x, end='')
print()



