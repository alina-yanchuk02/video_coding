from Golomb import *

test_golomb = Golomb()
numero_a_converter = 0
m=4
resultado = test_golomb.encode(numero_a_converter,m)
print(resultado)

numero_desconvertido = test_golomb.decode(resultado[0],resultado[1],m)
print(numero_desconvertido)
