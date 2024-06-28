import tkinter as tk
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image, ImageTk
from multiprocessing import Process
import cv2 as cv2
import time
from threading import Thread

import imageio.v3 as iio

# vid = imageio.get_reader('<video0>')

vid = iio.imiter("<video1>")
frame=0
a=time.time()
ct=time.time()
#(x0,y0,x1,y1)
pos=(100,100,300,300)
root = tk.Tk()
figure1 = plt.Figure(figsize=(6, 5), dpi=100)

ax = figure1.add_subplot(111)
ax.set_ylim(0,255)
fig = FigureCanvasTkAgg(figure1, root)
fig.get_tk_widget().pack(side=tk.LEFT, fill='both')

canvas = tk.Canvas(root, width=1280, height=720)
canvas.pack()

flag=False

stack=[]
stack_size=30
count=0
st=time.time()

def video_capture():
    global stack
    global count
    global st
    global stack_size
    frame=next(vid)
    img = ImageTk.PhotoImage(Image.fromarray(frame))

    if canvas.find_all!=[]:
        canvas.delete('image','sq')
    canvas.create_image(0, 0, image=img, anchor="nw",tags='image')
    canvas.create_rectangle(pos, tags='sq')
    canvas.image = img


    stack.append(frame)
    count+=1
    dt= time.time()-st
    if count>1:
        print(count/dt)
        st=time.time()
        stack_size=count
        count=0
        canvas.event_generate("<<event>>")
        stack=[]
    #upd_graph()
    canvas.after(1,video_capture)




size=300
colors=[[0]*size,[0]*size,[0]*size]
x1=np.arange(size)
def upd_graph(event):
    global stack
    global pos
    global flag
    flag=True
    #[y0:y1,x0:x1,chanel]
    for frame in stack:
        colors[0].append(np.average(frame[pos[0]:pos[2],pos[1]:pos[3],0]))
        colors[1].append(np.average(frame[pos[0]:pos[2],pos[1]:pos[3],1]))
        colors[2].append(np.average(frame[pos[0]:pos[2],pos[1]:pos[3],2]))
    del colors[0][0:stack_size]
    del colors[1][0:stack_size]
    del colors[2][0:stack_size]
    ax.clear()
    ax.plot(x1,colors[0], c='tab:red')
    ax.plot(x1,colors[1], c='tab:green')
    ax.plot(x1,colors[2], c='tab:blue')
    ax.set_ylim(0,255)
    fig.draw_idle()
    flag=False



def move(event):
    global pos
    print(event.keysym)
    shift=5
    size=2
    if event.keysym=='b':
        pos=(pos[0]-size,pos[1]-size,pos[2]+size,pos[3]+size)    
    if event.keysym=='m':
        pos=(pos[0]+size,pos[1]+size,pos[2]-size,pos[3]-size)    
    if event.keysym=="Left":
        pos=(pos[0]-shift,pos[1],pos[2]-shift,pos[3])
    if event.keysym=="Right":
        pos=(pos[0]+shift,pos[1],pos[2]+shift,pos[3])
    if event.keysym=="Up":
        pos=(pos[0],pos[1]-shift,pos[2],pos[3]-shift)
    if event.keysym=="Down":
        pos=(pos[0],pos[1]+shift,pos[2],pos[3]+shift) 
    print(pos,pos[2]-pos[0])

root.bind("<<event>>",upd_graph)
for i in ('<Up>','<Down>','<Left>','<Right>','<m>','<b>'):
    root.bind(i,move)
root.after(10,video_capture)
root.mainloop()

