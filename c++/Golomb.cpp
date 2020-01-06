#include <string>
#include <iostream>
#include <exception>
#include <fstream>
#include<bits/stdc++.h>
#include "Golomb.h"

using namespace std;

        Golomb::Golomb(){
            number=0;
            m=4;
            unicode="";
            binary="";
        
        };

        Golomb::Golomb(int number,int m){
            number=number;
            m=m;
            unicode="";
            binary="";
        
        };

        Golomb::Golomb(std::string unicode, std::string binary, int m){
            number=0;
            m=m;
            unicode=unicode;
            binary=binary;
        
        };

        Golomb::~Golomb() {

        };



       std::string* Golomb::encode(){

            std::string* qr=new std::string[2];
            int i=1;
            int j=0;
            int q,r;
            std::string unicode="";
            std::string binary="";
            std::string binario_string;
            int binario;


            if (number>=0){

                if(m!=0){

                    if(ceil(log2(m)) == floor(log2(m))){

                        q=number/m;

                        r=number-(q*m);

                        if (q!=0) {

                            while(true){
                                unicode.append("0");
                                i++;
                                if (i==q+1) break;
                            }

                        unicode.append("1");


                        }



                        while (r > 0) {

                            binario = r % 2;
                            binario_string=to_string(binario);
                            binary.insert (0,binario_string);
                            r = r / 2;
                            i++;

                        }

                        qr[0]=unicode;
                        qr[1]=binary;



                        return qr;
                    }

                    else cout << "m tem de ser potência de 2";
                }

                else cout << "m tem de ser positivo";
            }

            else {
                cout << "O número tem de ser um inteiro positivo!";
                exit(1);
            }
        }



        int Golomb::decode(){

            int numero;
            int resultado;
            int q;
            int r=0;
            int base=1;
            int resto;


            int carateres=unicode.length();
            q=carateres-1;

            int binary_int=std::stoi(binary);
            cout << binary_int << "\n";
            int temp=binary_int;


            while (temp) {

                int last_digit = temp % 10;

                temp = temp / 10;

                r += last_digit * base;

                base = base * 2;
            }


            numero=r+(q*m);
            resultado= numero;
            return resultado;


        }









// TEST GOLOMB:



int main(){

    Golomb test_golomb(11,4);
    std::string *result;
    test_golomb.encode();
    cout << "Resultado da conversão do inteiro para Golomb: "+result[0]+result[1]+"\n";


    Golomb test_golomb2(result[0],result[1],4);
    int numero_desconvertido;
    numero_desconvertido=test_golomb.decode();
    cout << "Resultado de conversão de Golomb para inteiro: " << numero_desconvertido << "\n";






}
