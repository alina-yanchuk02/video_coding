#include <string>
#include <iostream>
#include <exception>
#include <fstream>

using namespace std;

class BitStream{

    public:
    
        int read_one_bit(string file){

            try{

                ifstream f(file, ios::binary | ios::in);

                char c;
                int bit_int;

                while (f.get(c)){

                    for (int i = 7; i >= 0; i--) {

                        bit_int=((c >> i) & 1);
                        break;

                    } 

                    break;
                }
                    
                return bit_int;
                    

            }catch(exception& e){
                cout << "An exception occurred when reading from the given file. Exception  " << e.what();
            }

            
        };



        bool write_one_bit(int bit){
            
            int number=3;
            ofstream file;
            file.open("one_bit_output.bin", ios_base::out | ios_base::binary);

            if (!file.is_open()) {
                cout << "Não deu para criar o ficheiro de output." << endl;
            }
            else {
                file.write((char*)&number, sizeof(int));
            };

            return true;
            
        }




    /////////////////////////////////////





        int * read_bits(string file, int n){

            try{
                
                ifstream f(file, ios::binary | ios::in);
                
                char c;
                static int bits_int[100];
                int contador=0;
                int bit;
                int j=0;

                while (f.get(c)){
                    
                    for (int i = 7; i >= 0; i--) {

                        bit=((c >> i) & 1);
    
                        bits_int[j]=bit;
                        j++;
                        contador=contador+1;

                        if (contador==n) break;

                    } 

                    if (contador==n) break;
                    
                   
                }


                return bits_int;

            }catch(exception& e){
                cout << "An exception occurred when reading from the given file. Exception  " << e.what();
            }

            
        };

    

  
        bool write_bits(int bits[],int size_array){
            
            const char* FILENAM = "n_bits_output.bin";
            int bit;
            
            ofstream o(FILENAM,ios::binary);
            for(int i=0;i<size_array;i++){
                bit=bits[i];
                o.write((char*)&bit,sizeof(bit));
            }
            o.close();
            return true;
        };


};

int main(){
    BitStream* test_stream = new BitStream();
    int *bits;
    int bit;
    int n=40;



    bit=test_stream->read_one_bit("topo.bin");
    cout << "Primeiro bit: " << bit;
    cout << "\n";



    bits=test_stream->read_bits("topo.bin",n);
    cout << "Primeiros " << n << " bits: ";
    for ( int i = 0; i < n; i++ ) {
        cout << bits[i];
    }
    cout << "\n";




///////////////////






    test_stream->write_one_bit(bit);

    

    test_stream->write_bits(bits,n);
 




 
    bit=test_stream->read_one_bit("one_bit_output.bin");
    cout << "Primeiro bit do output file: " << bit;
    cout << "\n";



    bits=test_stream->read_bits("one_bit_output",n);
    cout << "Primeiros " << n << " bits do output file: ";
    for ( int i = 0; i < n; i++ ) {
        cout << bits[i];
    }
    cout << "\n";


}
    



 