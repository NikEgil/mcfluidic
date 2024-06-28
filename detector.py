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

vid = iio.imiter("<video0>")
frame=None
a=time.time()
ct=time.time()
#(x0,y0,x1,y1)
pos=(100,100,105,105)
root = tk.Tk()
figure1 = plt.Figure(figsize=(6, 5), dpi=100)

ax = figure1.add_subplot(111)
ax.set_ylim(0,255)
fig = FigureCanvasTkAgg(figure1, root)
fig.get_tk_widget().pack(side=tk.LEFT, fill='both')

label_video= tk.Label()
label_video.pack(side=tk.RIGHT, fill='both')

count=0
st=time.time()
def video_capture():
    global frame
    global count
    global st
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





size=50
colors=[[0]*size,[0]*size,[0]*size]
x1=np.arange(size)
def upd_graph():
    global frame
    global pos
    #[y0:y1,x0:x1,chanel]
    red=frame[pos[0]:pos[2],pos[1]:pos[3],0]
    green=frame[pos[0]:pos[2],pos[1]:pos[3],1]
    blue=frame[pos[0]:pos[2],pos[1]:pos[3],2]
    colors[0].append(np.average(red))
    colors[1].append(np.average(green))
    colors[2].append(np.average(blue))
    colors[0].pop(0)
    colors[1].pop(0)
    colors[2].pop(0)
    ax.clear()
    ax.plot(x1,colors[0], c='tab:red')
    ax.plot(x1,colors[1], c='tab:green')
    ax.plot(x1,colors[2], c='tab:blue')
    ax.set_ylim(0,255)
    fig.draw()



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
    print(pos)

root.bind("<<event>>",upd_graph)
for i in ('<Up>','<Down>','<Left>','<Right>','<m>','<b>'):
    print(i)
    root.bind(i,move)
root.after(1,video_capture)
root.mainloop()

