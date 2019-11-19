from array import array

class BitStream:
    def __init__(self):
        self.bitstream = []
    def __eq__(self):
        pass
    def __str__(self):
        pass
    def read_file(self,filename):
        f=open(filename, "rb")
        for byte in f.read():
            print(byte)
            for i in range(8):
                self.bitstream.append((byte >> i) & 1)
    def write_file(self):
        pass
    def read_a_bit(self):
        pass
    def write_a_bit(self):
        pass
    def read_n_bits(self):
        pass
    def write_n_bits(self):
        pass
