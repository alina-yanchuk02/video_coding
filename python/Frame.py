import numpy
from Golomb import *
from BitStream import *


class Frame:
    def __init__(self, height, width):
        self.height = (height + 15) // 16 * 16
        self.width = (width + 31) // 32 * 32
        self.YUV = None
        self.Y = None
        self.U = None
        self.V = None

    def codificador(self):
        counter = 0
        real = 0
        bitstream = BitStream()
        for matriz in [self.Y,self.U,self.V]:
            for y in range(0,self.height):
                for x in range(0,self.width):
                    p = 0
                    if y == 0 or x == 0:
                        bitstream.addBit(int(0))
                        l = int(matriz[y][x])
                    else:
                        a = int(matriz[y][x-1])
                        b = int(matriz[y-1][x])
                        c = int(matriz[y-1][x-1])

                        p = min(a,b,c,a+b-c,a+(b-c)/2,b+(a-c)/2,(a+b)/2)
                        l = int(matriz[y][x]) - int(p)

                        if l < 0:
                            bitstream.addBit(int(1))
                        if l >= 0:
                            bitstream.addBit(int(0))


                    counter+=1
                    golomb = Golomb()
                    g = golomb.encode(abs(l),4)


                    for bit in "".join(g):
                        bitstream.addBit(int(bit))

                    x+=1

                y+=1

        return bitstream

    def descodificar(self,Y,U,V):
        yuv = 0

        for matriz in [Y,U,V]:
            yuv +=1
            new_matriz = numpy.array([[0]* self.width ] * self.height)

            for y in range(0,self.height):
                for x in range(0,self.width):
                    p = 0
                    if y == 0 or x == 0:
                        new_matriz[y,x] = int(matriz[y][x])

                    else:
                        a = int(new_matriz[y,x-1])
                        b = int(new_matriz[y-1,x])
                        c = int(new_matriz[y-1,x-1])

                        p = min(a,b,c,a+b-c,a+(b-c)/2,b+(a-c)/2,(a+b)/2)
                        #print(matriz[y][x])
                        new_matriz[y,x] = int(matriz[y][x]) + int(p)

            if yuv == 1:
                self.Y = new_matriz
            if yuv == 2:
                self.U = new_matriz
            if yuv == 3:
                self.V = new_matriz


    def load_frame_descodificado(self):
        self.YUV = numpy.dstack((self.Y, self.U, self.V))[:self.height, :self.width, :].astype(numpy.float)

        self.YUV[:, :, 0] = self.YUV[:, :, 0] - 16
        self.YUV[:, :, 1:] = self.YUV[:, :, 1:] - 128
        M = numpy.array([[1.164,  2.017,  0.000],
                    [1.164, -0.392, -0.813],
                    [1.164,  0.000,  1.596]])

        BGR = self.YUV.dot(M.T).clip(0, 255).astype(numpy.uint8)
        return BGR


class Frame_4_4_4(Frame):
    def __init__(self, height, width):
        super().__init__(height, width)

    def load_frame(self, read):
        self.Y = numpy.fromfile(read, dtype=numpy.uint8, count=self.width * self.height).reshape(self.height, self.width)

        self.U = numpy.fromfile(read, dtype=numpy.uint8, count=self.width * self.height).reshape(self.height, self.width)

        self.V = numpy.fromfile(read, dtype=numpy.uint8, count=self.width * self.height).reshape(self.height, self.width)

        self.YUV = numpy.dstack((self.Y, self.U, self.V))[:self.height, :self.width, :].astype(numpy.float)

        self.YUV[:, :, 0] = self.YUV[:, :, 0] - 16
        self.YUV[:, :, 1:] = self.YUV[:, :, 1:] - 128
        M = numpy.array([[1.164,  2.017,  0.000],
                    [1.164, -0.392, -0.813],
                    [1.164,  0.000,  1.596]])

        BGR = self.YUV.dot(M.T).clip(0, 255).astype(numpy.uint8)
        return BGR


class Frame_4_2_2(Frame):
    def __init__(self, height, width):
        super().__init__(height, width)

    def load_frame(self, read):

        self.Y = numpy.fromfile(read, dtype=numpy.uint8, count=self.width * self.height).reshape((self.height, self.width))

        self.U = numpy.fromfile(read, dtype=numpy.uint8, count=(self.width//2)*(self.height//2)).reshape((self.height//2, self.width//2)).repeat(2, axis=0).repeat(2, axis=1)

        self.V = numpy.fromfile(read, dtype=numpy.uint8, count=(self.width//2)*(self.height//2)).reshape((self.height//2, self.width//2)).repeat(2, axis=0).repeat(2, axis=1)

        self.YUV = numpy.dstack((self.Y, self.U, self.V))[:self.height, :self.width, :].astype(numpy.float)

        self.YUV[:, :, 0] = self.YUV[:, :, 0] - 16
        self.YUV[:, :, 1:] = self.YUV[:, :, 1:] - 128
        M = numpy.array([[1.164,  2.017,  0.000],
                    [1.164, -0.392, -0.813],
                    [1.164,  0.000,  1.596]])

        BGR = self.YUV.dot(M.T).clip(0, 255).astype(numpy.uint8)
        return BGR


class Frame_4_2_0(Frame):

    def __init__(self, height, width):
        super().__init__(height, width)

    def load_frame(self, read):
        self.Y = numpy.fromfile(read, dtype=numpy.uint8, count=self.width * self.height).reshape((self.height, self.width))

        self.U = numpy.fromfile(read, dtype=numpy.uint8, count=(self.width//2)*(self.height//2)).reshape((self.height//2, self.width//2)).repeat(2, axis=0).repeat(2, axis=1)

        self.V = numpy.fromfile(read, dtype=numpy.uint8, count=(self.width//2)*(self.height//2)).reshape((self.height//2, self.width//2)).repeat(2, axis=0).repeat(2, axis=1)

        self.YUV = numpy.dstack((self.Y, self.U, self.V))[:self.height, :self.width, :].astype(numpy.float)

        self.YUV[:, :, 0] = self.YUV[:, :, 0] - 16
        self.YUV[:, :, 1:] = self.YUV[:, :, 1:] - 128
        M = numpy.array([[1.164,  2.017,  0.000],
                    [1.164, -0.392, -0.813],
                    [1.164,  0.000,  1.596]])


        BGR = self.YUV.dot(M.T).clip(0, 255).astype(numpy.uint8)
        return BGR
