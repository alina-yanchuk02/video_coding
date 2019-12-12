from Frame import *
import numpy as np
import cv2 as cv2


class Video_Player:

    def __init__(self, file):

        self.file = file   
        self.width = 0
        self.height = 0
        self.fps = 0
        self.contador=0
        


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
            
            frame = Frame_4_2_0(self.height, self.width)

            while True:

                read.readline()
                frame_image=frame.load_frame(read)
                
                
                cv2.imshow('image', frame_image)
                cv2.waitKey(1)

                if self.contador==self.width:
                    break

                self.contador=self.contador+1

            cv2.destroyAllWindows()

if __name__ == "__main__":
    video = Video_Player("video.y4m")
    video.play_video()