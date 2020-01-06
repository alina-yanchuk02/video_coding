
#define INC_07_GOLOMB_H

#include <iostream>


class Golomb{

    private:

        int number, m;
        std::string unicode, binary;

    public:

        Golomb();

        Golomb(std::string unicode, std::string binary, int m);

        Golomb(int number,int m);

        ~Golomb();

        std::string *encode();

        int decode();


};




