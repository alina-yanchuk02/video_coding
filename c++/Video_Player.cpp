#include <string>
#include <iostream>
#include <exception>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;


class VideoPlayer{

    public:

        int height_num,width_num;
        std::string fps,v;

        void read_video_file(string file){


            char c;
            std::string line;
            std::string delimiter = " ";

            ifstream myfile;
            myfile.open(file);

            if(!myfile.is_open()) {
                perror("Erro ao abrir o ficheiro!");
                exit(EXIT_FAILURE);
            }

            getline(myfile, line);



            std::istringstream buf(line);
            std::istream_iterator<std::string> beg(buf), end;

            std::vector<std::string> tokens(beg, end);

            std::string width;
            width=tokens[1];
            width.erase(std::remove(width.begin(), width.end(), 'W'), width.end());
            width_num=stoi(width);

            std::string height;
            height=tokens[2];
            height.erase(std::remove(height.begin(), height.end(), 'H'), height.end());
            height_num=stoi(height);


            fps=tokens[3];
            fps.erase(std::remove(fps.begin(), fps.end(), 'F'), fps.end());

            v=tokens[6];

            if (v=="C422"){
                cout << v;

            }

            if (v=="C444"){
                cout << v;

            }


            getline(myfile, line);

            int size=(width_num * 2) * height_num;
            char* frame_row = new char[size];
            int contador=0;


            linha=getline(myfile,line);
            cout << linha;




        };







};

int main(){

    VideoPlayer* test_player = new VideoPlayer();

    test_player->read_video_file("ducks_take_off_420_720p50.y4m");



}
