import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image, ImageTk
import cv2 as cv2
import time
from threading import Thread

import imageio.v3 as iio


vid = iio.imiter("<video0>")
frame=0

a=time.time()
ct=time.time()
#(x0,y0,x1,y1)
pos=(294, 570, 474, 750)
#нужно чтобы fullhd в hd перемасштабировать
pos_rs=list(np.array(pos)/1.5)
root = tk.Tk()



def upd_graph(event):
    global pereris
    #[y0:y1,x0:x1,chanel
    colors[0].append(np.average(frame[pos[1]:pos[3],pos[0]:pos[2],0]))
    colors[1].append(np.average(frame[pos[1]:pos[3],pos[0]:pos[2],1]))
    colors[2].append(np.average(frame[pos[1]:pos[3],pos[0]:pos[2],2]))
    del colors[0][0]
    del colors[1][0]
    del colors[2][0]
    ax.clear()
    ax.plot(x1,colors[0], c='tab:red')
    ax.plot(x1,colors[1], c='tab:green')
    ax.plot(x1,colors[2], c='tab:blue')
    ax.set_ylim(0,255)
    fig.draw_idle()
    pereris= False



root.bind("<<event1>>",upd_graph)


figure1 = plt.Figure(figsize=(3, 5), dpi=150)

ax = figure1.add_subplot(111)
ax.set_ylim(0,255)
fig = FigureCanvasTkAgg(figure1, root)
fig.get_tk_widget().pack(side=tk.LEFT, fill='both')

canvas = tk.Canvas(root, width=1280, height=720)
canvas.pack()

flag=False


size=150
colors=[[0]*size,[0]*size,[0]*size]

pereris=False
q=time.time()
def video_capture():
    global pereris
    global frame
    global q
    frame=next(vid)
    # frame2=frame[pos[1]:pos[3],pos[0]:pos[2]]
    # img = ImageTk.PhotoImage(Image.fromarray(frame2))
    # img = ImageTk.PhotoImage(Image.fromarray(frame))
    img = Image.fromarray(frame)
    ri=img.resize((1280,720))
    img=ImageTk.PhotoImage(ri)
    if not pereris:
        pereris=True
        root.event_generate("<<event1>>")
    if canvas.find_all!=[]:
        canvas.delete('image','sq')
    canvas.create_image(0,0, image=img,anchor="nw",tags='image')
    canvas.create_rectangle(pos_rs, tags='sq')
    canvas.image = img
    print((time.time()-q))
    q=time.time()
    canvas.after(1,video_capture)
    



x1=np.arange(size)



def move(event):
    global pos
    global pos_rs
    print(event.keysym)
    print(len(frame),len(frame[0]))
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


for i in ('<Up>','<Down>','<Left>','<Right>','<m>','<b>'):
    root.bind(i,move)
root.after(10,video_capture)
root.mainloop()

