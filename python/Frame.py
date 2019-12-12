import numpy 

      


class Frame_4_4_4():
    def __init__(self, height, width):
        self.height = (height + 15) // 16 * 16
        self.width = (width + 31) // 32 * 32
        self.YUV = None

    def load_frame(self, read):
        self.Y = numpy.fromfile(read, dtype=numpy.uint8, count=self.width * self.height).reshape((self.height, self.width))
    
        self.U = numpy.fromfile(read, dtype=numpy.uint8, count=self.width *
                                self.height).reshape((self.height, self.width))
        self.V = numpy.fromfile(read, dtype=numpy.uint8, count=self.width *
                                self.height).reshape((self.height, self.width))

        self.YUV = numpy.dstack((self.Y, self.U, self.V))[
            :self.height, :self.width, :].astype(numpy.float)

        self.YUV[:, :, 0] = self.YUV[:, :, 0] - 16   
        self.YUV[:, :, 1:] = self.YUV[:, :, 1:] - 128  
        M = numpy.array([[1.164,  2.017,  0.000],    
                    [1.164, -0.392, -0.813],    
                    [1.164,  0.000,  1.596]])

        BGR = self.YUV.dot(M.T).clip(0, 255).astype(numpy.uint8)
        return BGR


class Frame_4_2_2():
    def __init__(self, height, width):
        self.height = (height + 15) // 16 * 16
        self.width = (width + 31) // 32 * 32
        self.YUV = None

    def load_frame(self, read):

        self.Y = numpy.fromfile(read, dtype=numpy.uint8, count=self.width * self.height).reshape((self.height, self.width))
    
        self.U = numpy.fromfile(read, dtype=numpy.uint8, count=self.width * self.height).reshape((self.height, self.width))
        
        self.V = numpy.fromfile(read, dtype=numpy.uint8, count=(self.width//2)*(self.height//2)).reshape((self.height//2, self.width//2)).repeat(2, axis=0).repeat(2, axis=1)

        self.YUV = numpy.dstack((self.Y, self.U, self.V))[
            :self.height, :self.width, :].astype(numpy.float)

        self.YUV[:, :, 0] = self.YUV[:, :, 0] - 16  
        self.YUV[:, :, 1:] = self.YUV[:, :, 1:] - 128  
        M = numpy.array([[1.164,  2.017,  0.000],    
                    [1.164, -0.392, -0.813],    
                    [1.164,  0.000,  1.596]])

        BGR = self.YUV.dot(M.T).clip(0, 255).astype(numpy.uint8)
        return BGR


class Frame_4_2_0():
    
    def __init__(self, height, width):
        self.height = (height + 15) // 16 * 16
        self.width = (width + 31) // 32 * 32
        self.YUV = None

    def load_frame(self, read):
        self.Y = numpy.fromfile(read, dtype=numpy.uint8, count=self.width *
                                self.height).reshape((self.height, self.width))
        
       
        self.U = numpy.fromfile(read, dtype=numpy.uint8, count=(
            self.width//2)*(self.height//2)).reshape((self.height//2, self.width//2)).repeat(2, axis=0).repeat(2, axis=1)
        self.V = numpy.fromfile(read, dtype=numpy.uint8, count=(
            self.width//2)*(self.height//2)).reshape((self.height//2, self.width//2)).repeat(2, axis=0).repeat(2, axis=1)

        self.YUV = numpy.dstack((self.Y, self.U, self.V))[
            :self.height, :self.width, :].astype(numpy.float)

        self.YUV[:, :, 0] = self.YUV[:, :, 0] - 16   
        self.YUV[:, :, 1:] = self.YUV[:, :, 1:] - 128  
        M = numpy.array([[1.164,  2.017,  0.000],    
                    [1.164, -0.392, -0.813],    
                    [1.164,  0.000,  1.596]])

        
        BGR = self.YUV.dot(M.T).clip(0, 255).astype(numpy.uint8)
        print(BGR)
        return BGR