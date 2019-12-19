import numpy


class Frame:
    def __init__(self, height, width):
        self.height = (height + 15) // 16 * 16
        self.width = (width + 31) // 32 * 32
        self.YUV = None
        self.Y = None
        self.U = None
        self.V = None

    def jpeg(self,matriz):
        print("-----------------")
        new_matriz = [[0]*self.width]*self.height
        for y in range(1,len(self.Y)):
            for x in range(1,len(self.Y[0])):
                if y == 0 or x == 0:
                    new_matriz[y][x] = self.Y[y][x]
                else:
                    a = self.Y[y][x-1]
                    b = self.Y[y-1][x]
                    c = self.Y[y-1][x-1]

                    if c >= max(a,b):
                        new_matriz[y][x] = min(a,b)
                    elif c <= min(a,b):
                        new_matriz[y][x] = min(a,b)
                    else:
                        new_matriz[y][x] = a + b - c
                x+=1
            y+=1


class Frame_4_4_4(Frame):
    def __init__(self, height, width):
        super().__init__(height, width)

    def load_frame(self, read):
        self.Y = numpy.fromfile(read, dtype=numpy.uint8, count=self.width * self.height).reshape(self.height, self.width)
        print(self.Y)
        self.U = numpy.fromfile(read, dtype=numpy.uint8, count=self.width * self.height).reshape(self.height, self.width)

        self.V = numpy.fromfile(read, dtype=numpy.uint8, count=self.width * self.height).reshape(self.height, self.width)

        self.YUV = numpy.dstack((self.Y, self.U, self.V))[:self.height, :self.width, :].astype(numpy.float)

        self.YUV[:, :, 0] = self.YUV[:, :, 0] - 16
        self.YUV[:, :, 1:] = self.YUV[:, :, 1:] - 128
        M = numpy.array([[1.164,  2.017,  0.000],
                    [1.164, -0.392, -0.813],
                    [1.164,  0.000,  1.596]])

        BGR = self.YUV.dot(M.T).clip(0, 255).astype(numpy.uint8)
        print("----------------------------------------------")
        print(len(BGR))
        print(len(BGR[0]))
        return BGR


class Frame_4_2_2(Frame):
    def __init__(self, height, width):
        super().__init__(height, width)

    def load_frame(self, read):

        self.Y = numpy.fromfile(read, dtype=numpy.uint8, count=self.width * self.height).reshape((self.height, self.width))

        self.U = numpy.fromfile(read, dtype=numpy.uint8, count=self.width * self.height).reshape((self.height, self.width))

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
