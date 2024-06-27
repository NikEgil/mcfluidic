import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image, ImageTk, ImageDraw
from multiprocessing import Process
import cv2 as cv2
import time
from threading import Thread

import imageio.v3 as iio

# vid = imageio.get_reader('<video0>')

vid = iio.imiter("<video1>")
frame=None
a=time.time()
ct=time.time()
fps=0
x=100
y=100
pos=(100,100,105,105)
root = tk.Tk()
figure1 = plt.Figure(figsize=(6, 5), dpi=100)

ax = figure1.add_subplot(111)
#ax.set_ylim(0,255)
fig = FigureCanvasTkAgg(figure1, root)
fig.get_tk_widget().pack(side=tk.LEFT, fill='both')

label_video= tk.Label()
label_video.pack(side=tk.RIGHT, fill='both')


def video_capture():
    global frame
    frame=next(vid)
    captured_image = Image.fromarray(frame) 
    m = ImageDraw.Draw(captured_image)
    m.rectangle(pos, outline='red',  width=4)
    photo_image = ImageTk.PhotoImage(image=captured_image) 
    label_video.photo_image = photo_image 
    label_video.configure(image=photo_image)
    
   # label_video.event_generate("<<event>>")
    upd_graph()
    label_video.after(1,video_capture)





size=300
aaa=[[0]*size,[0]*size,[0]*size]
x1=np.arange(size)
def upd_graph():
    global frame
    global pos
    print(pos[0],pos[1],pos[2],pos[3])

    red=frame[pos[0]:pos[2]][pos[1]:pos[3]][0]
    aaa[1].append(frame[x][y][1])
    aaa[2].append(frame[x][y][2])
    aaa[0].pop(0)
    r=np.sum(red)
   # r=np.sum(r,axis=0)
    print(red)
    print(r)
    aaa[0].append(r)
    # aaa[1].pop(0)
    # aaa[2].pop(0)
    ax.clear()
    ax.plot(x1,aaa[0], c='tab:red')
    # ax.plot(x1,aaa[1], c='tab:green')
    # ax.plot(x1,aaa[2], c='tab:blue')
    fig.draw()



def move(event):
    global pos
    print(event)
    print(event.keysym)
    print(event.state)
    if event.keysym=='b':
        pos=(pos[0]-2,pos[1]-2,pos[2]+2,pos[3]+2)    
    if event.keysym=='m':
        pos=(pos[0]+2,pos[1]+2,pos[2]-2,pos[3]-2)    
    if event.keysym=="Left":
        pos=(pos[0]-10,pos[1],pos[2]-10,pos[3])
    if event.keysym=="Right":
        pos=(pos[0]+10,pos[1],pos[2]+10,pos[3])
    if event.keysym=="Up":
        pos=(pos[0],pos[1]-10,pos[2],pos[3]-10)
    if event.keysym=="Down":
        pos=(pos[0],pos[1]+10,pos[2],pos[3]+10) 


root.bind("<<event>>",upd_graph)
for i in ('<Up>','<Down>','<Left>','<Right>','<m>','<b>'):
    print(i)
    root.bind(i,move)
root.after(1,video_capture)
root.mainloop()

