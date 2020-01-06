from BitStream import *

bitstream = BitStream()
bitstream.setFileInput("topo.bin")
bitstream.read_file()
bit = bitstream.read_a_bit(100)
print(bit)
bits = bitstream.read_n_bits(200,20)
print(bits)

bitstream.setFileOutput("test.bin")
bitstream.write_file()


b = BitStream()
b.setFileInput("test.bin")
b.read_file()
bit = b.read_a_bit(100)
print(bit)
bits = b.read_n_bits(200,20)
print(bits)
