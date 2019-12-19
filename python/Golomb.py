import math

class Golomb:
    def __init__(self):
        pass
    def encode(self,number,m):
        qr=[]
        i=1
        j=0
        unicode = ""
        binary = ""

        if number == 0:
            return ['0','0'] 
        elif number >= 0:
            if m != 0:
                if math.ceil(math.log2(m)) == math.floor(math.log2(m)):
                    q = math.floor(number/m)
                    r=math.floor(number-(q*m))
                    if q !=0:
                        while(True):
                            unicode+="0"
                            i+=1
                            if i == q+1:
                                break
                        unicode+="1"
                    while (r > 0):
                        binario = math.floor(r % 2)
                        binario_string = str(binario)
                        binary = binario_string + binary
                        r = math.floor(r/2)
                        i+=1
                    qr.append(unicode)
                    qr.append(binary)
                    return qr
                else:
                    print("m tem de ser potência de 2")
            else:
                print("m tem de ser positivo")
        else:
            print("O número tem de ser um inteiro positivo!")



    def decode(self,unicode,binary,m):
        carateres = len(unicode)
        q=carateres-1
        binary_int = int(binary)
        temp = binary_int
        r=0
        base=1
        while(temp):
            last_digit = math.floor(temp % 10)
            temp = math.floor(temp / 10)
            r += last_digit * base
            base = base * 2

        numero = r+(q*m)
        return numero
