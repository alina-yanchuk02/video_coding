from Golomb import *

test_golomb = Golomb()
numero_a_converter = 5
m=4
resultado = test_golomb.encode(numero_a_converter,m)
print(resultado)

numero_desconvertido = test_golomb.decode(resultado[0],resultado[1],m)
print(numero_desconvertido)
numero_desconvertido = test_golomb.decode('000000000000001','10',m)
print(numero_desconvertido)

test_golomb = Golomb()
'''for i in range(0,256):
    numero_a_converter = i
    m=4
    resultado = test_golomb.encode(numero_a_converter,m)
    print(resultado)

    numero_desconvertido = test_golomb.decode(resultado[0],resultado[1],m)
    print(numero_desconvertido)'''
