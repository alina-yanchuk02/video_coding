from Frame import *
import numpy as np
import cv2 as cv2
from datetime import datetime
import os

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
                cv2.waitKey(1000)
                if i == 2:
                    break

            cv2.destroyAllWindows()


    def codificador(self):

        with open(self.file, "rb") as read:

            header = read.readline().decode("UTF-8")
            ## linha YUV4MPEG2 W352 H288 F30:1 Ip A128:117 C422

            header = header.split(" ")

            self.width = int(header[1].replace("W", ""))

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
                frame_image=frame.load_frame(read)
                bst_frame = frame.codificador()
                bitstream.write_n_bits(bst_frame.bitstream)
                if i == 2:
                    break

    def descodificador(self, file, height, width):
        golomb = Golomb()
        bitstream = BitStream()
        bitstream.setFileInput(file)
        bitstream.read_file()
        decode = []

        unicode = ""
        binary = ""
        count = 0
        sinal = 0
        q=0

        for bit in bitstream.bitstream:
            if len(unicode) == 0 and q == 0:
                sinal = bit
                q+=1
            elif len(unicode) == 0 and q == 1:
                unicode += str(bit)
            elif unicode[-1] != '1':
                unicode += str(bit)
            else:
                binary += str(bit)
            if len(unicode) >= 1 and len(binary) == 2:
                g = golomb.decode(unicode,binary,4)
                if sinal == 0:
                    decode.append(g)
                if sinal == 1:
                    g = g * (-1)
                    decode.append(g)
                unicode = ""
                binary = ""
                q=0
                count+=1


        i=0
        list_frames=[]
        size = height * width * 3
        while i<len(decode):
            list_frames.append(decode[i:i+size])
            i+=size

        frames = []

        for d in list_frames:

            i=0
            yuv = []
            size = height * width
            while i<len(d):
                yuv.append(d[i:i+size])
                i+=size

            yuv_done = []
            for ele in yuv:
                i = 0
                ele_done = []
                size = width
                while i<len(ele):
                    ele_done.append(ele[i:i+size])
                    i+=size
                yuv_done.append(ele_done)

            Y = yuv_done[0]
            U = yuv_done[1]
            V = yuv_done[2]


            frame = Frame(height,width)
            frame.descodificar(Y,U,V)

            frames.append(frame)


        return frames

    def play_video_descodificado(self,lista_frames):
        i = 0
        for frame in lista_frames:
            i+=1
            frame_image=frame.load_frame_descodificado()

            cv2.imshow('image', frame_image)
            cv2.waitKey(1000)
            if i == 2:
                break

        cv2.destroyAllWindows()



if __name__ == "__main__":
    video = Video_Player("ducks_take_off_420_720p50.y4m")
    video.play_video()
    video.codificador()
    frames = video.descodificador("jpeg.bin", video.height, video.width)
    video.play_video_descodificado(frames)
    os.remove("jpeg.bin")
