from Frame import *
import numpy as np
import cv2 as cv2
from datetime import datetime


class Video_Player:

    def __init__(self, file):

        self.file = file
        self.width = 0
        self.height = 0
        self.fps = 0
        self.contador=0
        self.type = None



    def play_video(self):

        with open(self.file, "rb") as read:

            header = read.readline().decode("UTF-8")
            ## linha YUV4MPEG2 W352 H288 F30:1 Ip A128:117 C422

            header = header.split(" ")

            self.width = int(header[1].replace("W", ""))
            print(self.width)

            self.height = int(header[2].replace("H", ""))

            self.fps = header[3].replace("F", "")

            read.readline()
            ## linha FRAME

            if len(header) > 6:
                if "C422" in header[6]:
                    frame = Frame_4_2_2(self.height, self.width)
                    self.type = 422
                if "C444" in header[6]:
                    frame = Frame_4_4_4(self.height, self.width)
                    self.type = 444
            else:
                frame = Frame_4_2_0(self.height, self.width)
                self.type = 420

            i = 0
            while read.readline() != b'':
                i+=1
                frame_image=frame.load_frame(read)

                cv2.imshow('image', frame_image)
                cv2.waitKey(1)
                if i == 10:
                    break

            cv2.destroyAllWindows()


    def codificador(self):

        with open(self.file, "rb") as read:

            header = read.readline().decode("UTF-8")
            ## linha YUV4MPEG2 W352 H288 F30:1 Ip A128:117 C422

            header = header.split(" ")

            self.width = int(header[1].replace("W", ""))
            print(self.width)

            self.height = int(header[2].replace("H", ""))

            self.fps = header[3].replace("F", "")

            read.readline()
            ## linha FRAME

            if len(header) > 6:
                if "C422" in header[6]:
                    frame = Frame_4_2_2(self.height, self.width)
                    self.type = 422
                if "C444" in header[6]:
                    frame = Frame_4_4_4(self.height, self.width)
                    self.type = 444
            else:
                frame = Frame_4_2_0(self.height, self.width)
                self.type = 420

            i=0
            bitstream = BitStream()
            bitstream.setFileOutput("jpeg.bin")
            while read.readline() != b'':
                i+=1
                print(i)
                inicio = datetime.now()
                frame_image=frame.load_frame(read)
                bst_frame = frame.codificador()
                fim = datetime.now()
                bitstream.write_n_bits(bst_frame.bitstream)
                l= fim -inicio
                print(l)
                if i == 10:
                    break

    def descodificador(self, file):
        pass


if __name__ == "__main__":
    video = Video_Player("ducks_take_off_420_720p50.y4m")
    #video.play_video()
    video.codificador()
    video.descodificador("jpeg.bin")
