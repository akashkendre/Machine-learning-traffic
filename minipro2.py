import time
from time import sleep
import Tkinter as tk 
from Tkinter import *

rk=Tk()
win=Canvas(rk,width=300,height=300)

win.pack()
def countdown(count):
    label['text']=count
    if count>0:
      root.after(1000,countdown,count-1)
root=tk.Tk()
label=tk.Label(root)
label.place(x=80,y=80)

def red(a):
          
    for i in range(a):        
        red=win.create_oval(50,50,150,150,fill='red')
        rk.update()
        print ("Time for red = ",a-i)
        time.sleep(1)
        countdown(a)
        
               
def green(a):
    for i in range(a):
        green=win.create_oval(50,50,150,150,fill='green')
        rk.update()
        print ("Time for green = ",a-i)
        time.sleep(1)
        countdown(a)

def orange(a):
    for i in range(a):
        orange=win.create_oval(50,50,150,150,fill='orange')
        rk.update()
        print ("Time for orange = ",a-i)
        time.sleep(1)
        countdown(a)

def lights():
    red=win.create_oval(50,50,150,150,fill='black')
    orange=win.create_oval(50,50,150,150,fill='black')
    green=win.create_oval(50,50,150,150,fill='black')

lights()
#root.destroy()
