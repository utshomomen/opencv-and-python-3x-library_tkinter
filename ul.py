from tkinter import *
import cv2
import numpy as np
import random
import numpy as np
import sys
from os import path

def EXIT():
    return  exit()
# comment of login


def LOGIN():



        buttonCam = Button(root, text='Camera', command = VIDEO)
        #buttonCAM.pack(side=DOWN)
        buttonCam.grid(row=0 , column = 6)
        #print ('Clicked')

        #button3 = Button(win,text = 'Flot Graph' , command = GRAPH)
        #button3.grid(row =1 , column =6)
        #button3.pack(side=RIGHT)

#######

def VIDEO():
 cam1 = cv2.VideoCapture(0)
 while True:
       ret,frame=cam1.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xFF == ord('q'):
           breakpoint()

           cam1.release()
           cv2.destroyAllWindows()

   ####

#project shhoild be here




######################################

root = Tk()
window =root.geometry("400x400")
root.title("hello")
root.iconbitmap('logo.ico')


label1 = Label(root, text="tittle:", bg='red',width=20)
label1.grid(row=0, column = 0 , sticky = E)


label2 = Label(root, text ='Advisor:', bg='red',fg = 'black', width =20)
label2.grid(row =1 , column = 0 , sticky =E)

entry1 = Entry (root)
entry1.grid(row=0 , column =1 ,ipadx =6)
entry1.insert(25, 'Ball and beam Balancing')

entry2= Entry(root)
entry2.grid(row =1 , column=1, ipadx=6)
entry2.insert(25,'utshomomen')

button1 = Button(root, text='OK', command = LOGIN)
button1.grid(row=2, column=0 , ipadx=2)

button2 = Button(root, text ='Quit',command = EXIT)
button2.grid(row=2, column =1, ipadx=2)

prompt =Label(text = "The Program was created by UTSHO MOMEN\nWelcome to FACE APP !", font=("Helvetica" ,8))
prompt.grid()



root.mainloop()