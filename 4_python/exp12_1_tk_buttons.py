#program to create three push buttons and change background colour wgeb button is clicked

from tkinter import *

class MyButton:
    #constructor
    def __init__(self,root):
        #create a frame as child to root window
        self.f = Frame(root, height=400, width=500)

        #let the frame will not shrink
        self.f.propagate(0)

        self.f.pack()

        #create three push butttons
        self.b1 = Button(self.f, text="RED", width=15, height=2, command = lambda: self.buttonClick(1))
        self.b2 = Button(self.f, text="GREEN", width=15, height=2, command = lambda: self.buttonClick(2))
        self.b3 = Button(self.f, text="BLUE", width=15, height=2, command = lambda: self.buttonClick(3))

        self.b1.pack()
        self.b2.pack()
        self.b3.pack()

    #method to be called when button is clicked
    def buttonClick(self,num):
        if num==1:
            self.f["bg"]="red"
        if num==2:
            self.f["bg"]="green"
        if num==3:
            self.f["bg"]="blue"

#create root window
root = Tk()
mb = MyButton(root)
                
