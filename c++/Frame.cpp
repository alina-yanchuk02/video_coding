#include <string>
#include <iostream>
#include <exception>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <iterator>
#include <algorithm>





using namespace std;


class Frame_4_4_4{

    public:

        int height,weight;
            int YUV[];
            int Y[];
            int U[];
            int V[];
            int BGR[];

        int * load_frame_4_4_4(height,width):

            

            height = floor((height + 15) / 16 * 16)
            width = floor((width + 31) / 32 * 32)
            YUV = []

            Y = numpy.fromfile(read, dtype=numpy.uint8, count=width * height).reshape((height, width))
        
            U = numpy.fromfile(read, dtype=numpy.uint8, count=width *
                                    height).reshape((height, width))
            V = numpy.fromfile(read, dtype=numpy.uint8, count=self.width *
                                    height).reshape((height, width))
            YUV = numpy.dstack((Y, U, V))[
                :height, :width, :].astype(numpy.float)

            YUV[:, :, 0] = YUV[:, :, 0] - 16   
            YUV[:, :, 1:] = YUV[:, :, 1:] - 128  
            M = np.array([[1.164,  2.017,  0.000],    
                        [1.164, -0.392, -0.813],    
                        [1.164,  0.000,  1.596]])

            BGR = YUV.dot(M.T).clip(0, 255).astype(numpy.uint8)
            return BGR



        

  


};

    



 


 