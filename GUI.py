import tkinter as Tk
from tkinter import *
import pyfirmata as fir
import time, pickle
import numpy as np
import pynput as pn

input = np.empty(3, dtype = float) #NOTE FIRST ELEMENT IS x, then y, then z... Looking for solution here.
switch = "" #The Selected number of switches
truth = np.empty(3, dtype = bool) #Array to questions "Is ____ positive"

window=Tk()
window.title('Input Box')
window.geometry("400x300+10+10")
lbl1=Label(window, text='x')
lbl2=Label(window, text='y')
lbl3=Label(window, text='z')
t1=Entry(window)
t2=Entry(window)
t3=Entry(window)
lbl1.place(x=100, y=50)
t1.place(x=200, y=50)
lbl2.place(x=100, y=100)
t2.place(x=200, y=100)
lbl3.place(x=100, y=150)
t3.place(x=200, y=150)
switch_dict = {"456":400, "56":800, "46":1600, "6": 3200, "45":6400, "5":12800, "4": 4000, "0":8000}
option_value = StringVar()
option_value.set("")
d1 = OptionMenu(window,option_value, *switch_dict)
d1.place(x=145, y=197, width=50)

def click(): #When Button clicked - Save value to these variables
    global input  #
    global switch #idk help
    global window #
    if(option_value.get() == ""): #Checks to see if you selected a number of switches
        print("Error, please remember to selected Number of switches active")
        return()
    else:
        switch = option_value.get()
        print(switch) #debug
        pass
    if (t1.get() == "" or t2.get() == "" or t3.get()== ""):
        print("Error, please enter dimensions")
        return()
    else:
        input[0] = float(t1.get()) 
        input[1] = float(t2.get())
        input[2] = float(t3.get())
        print(input) #debug check IGNORE
        pass
    window.quit()

b1=Button(window, text='Enter', command=click) #Submit button to save all inputed info
b1.place(x=100, y=200)
b2=Button(window, text='Exit', command=exit) #Exit button to destroy window, but not code
b2.place(x=200, y=200)

window.mainloop()

class digest: #Digesting the float type into the +/- orientaiton for Gantry
              #Asking the question "Is __ Postiive?
    if(input[0]<0.0):
        truth[0] = False
    else:
        truth[0] = True
    if(input[1]<0.0):
        truth[1] = False
    else:
        truth[1] = True
    if(input[2]<0.0):
        truth[2] = False
    else:
        truth[2] = True
    print(truth)