from array import array
import struct

class BitStream:
    def __init__(self):
        self.bitstream = []
        self.byteArray = []
        self.fileInput = ""
        self.fileOutput = ""

    def setFileInput(self,filename):
        self.fileInput = filename

    def setFileOutput(self,filename):
        self.fileOutput = filename

    def setBitstream(self,bitstream):
        self.bitstream = bitstream

    def addBit(self,bit):
        self.bitstream.append(bit)

    def read_file(self):
        f=open(self.fileInput, "rb")
        for byte in f.read():
            self.byteArray += [byte]
            for i in range(8):
                self.bitstream.append((byte >> i) & 1)

    def write_file(self):
        b = self.toBytes(self.bitstream)
        print(b == self.byteArray)
        f = open(self.fileOutput,"wb")
        f.write(bytes(b))

    def read_a_bit(self,pos):
        return self.bitstream[pos]

    def write_a_bit(self,pos):
        f = open(self.fileOutput,"ab")
        f.write(bytes(self.bitstream[pos]))

    def read_n_bits(self,pos,n_bits):
        n = 0
        r = []
        while n < n_bits:
            r += [self.bitstream[n]]
            n += 1
        return r

    def write_n_bits(self,pos_n_bits):
        b = self.toBytes(pos_n_bits)
        f = open(self.fileOutput,"ab")
        f.write(bytes(b))

    def toBytes(self,lista):
        return [int("".join(map(str, lista[i:i+8])), 2) for i in range(0, len(lista), 8)]
