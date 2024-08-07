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

vid = iio.imiter("<video0>")
frame=0

#(x0,y0,x1,y1)
pos=(152, 307, 248, 403)
pos_rs=list(np.array(pos)/1.5)


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
stack_size=300
count=0
st=time.time()
img=0
ct=time.time()
def video_capture():
    global stack
    global count
    global st
    global ct
    global stack_size
    global frame
    # st=time.time()
    frame=next(vid)
    stack.append(frame)
    count+=1
    if time.time()-ct>1: 
        dt= time.time()-ct
        print(count/dt)
        print(count)
        ct=time.time()
        stack_size=count
        count=0
        root.event_generate("<<event>>")
        stack=[]
    # ms=time.time()-st 
    # if ms<0.01:
    #     ms=10-ms*1000
    #     ms=int(ms)
    #     # print(st, ms)
    # else:
    #     ms=1
    root.after_idle(video_capture)


def a1():
    Thread(target=upd_can,daemon=True).start()

def upd_can():
    s=0
    while True:
        img1=Image.fromarray(frame)
        ri=img1.resize((1280,720))
        img=ImageTk.PhotoImage(ri)
        # img = ImageTk.PhotoImage(Image.fromarray(frame))
        if s==50:
            canvas.delete('image','sq','text')
            s=0
            print("del")
        canvas.create_image(0, 0, image=img, anchor="nw",tags='image')
        canvas.create_rectangle(pos_rs, tags='sq')
        canvas.create_text(20,20,fill='white', font=('16'), text=s,tags='text')
        s+=1
        
        



size=200
h=size-5
colors=[[0]*size,[0]*size,[0]*size]

a=0
def upd_graph(event):
    global stack
    global pos
    global flag
    global a
    colors=[[],[],[]]
    x1=np.arange(stack_size)
    #[y0:y1,x0:x1,chanel]
    for frame in stack:
        colors[0].append(np.average(frame[pos[1]:pos[3],pos[0]:pos[2],0]))
        colors[1].append(np.average(frame[pos[1]:pos[3],pos[0]:pos[2],1]))
        colors[2].append(np.average(frame[pos[1]:pos[3],pos[0]:pos[2],2])) 
    c=colors[-stack_size:]
    # del colors[0][0:stack_size]
    # del colors[1][0:stack_size]
    # del colors[2][0:stack_size]
    ax.clear()
    ax.plot(x1,colors[0], c='tab:red')
    ax.plot(x1,colors[1], c='tab:green')
    ax.plot(x1,colors[2], c='tab:blue')
    # ax.scatter(stack_size/2,240,s=200,color=(colors[0][stack_size]/255,colors[1][stack_size]/255,colors[2][stack_size]/255))
    ax.set_ylim(0,255)
    fig.draw_idle()
    flag=False


def save(mas):
    print(mas)
    with open(r"q.txt", "a") as file:
        for  line in mas:
            file.write(line + '\n')




def move(event):
    global pos
    global pos_rs
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
    pos_rs=list(np.array(pos)/1.5)


root.bind("<<event>>",upd_graph)
for i in ('<Up>','<Down>','<Left>','<Right>','<m>','<b>'):
    root.bind(i,move)
root.after(1,video_capture)
root.after(150,a1)
root.mainloop()

