import tkinter as tk
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


x=700
y=500
# Set the width and height 
fps=0

fr=[]
vid = iio.imiter("<video0>")   
def s(event):
    frame=next(vid)
    captured_image = Image.fromarray(frame) 
    photo_image = ImageTk.PhotoImage(image=captured_image) 
    can.photo_image = photo_image 
    can.configure(image=photo_image)
    ch()
      

size=30
aaa=[[0]*size,[0]*size,[0]*size]
def ch():

    x1=np.arange(size)

    aaa[0].append(np.random.randint(0,255))
    # aaa[1].append(np.random.randint(0,255))
    # aaa[2].append(np.random.randint(0,255))
    aaa[0].pop(0)
    # aaa[1].pop(0)
    # aaa[2].pop(0)
    ax2.clear()
    ax2.scatter(x1,aaa[0], c='tab:red')
    # ax2.scatter(x1,aaa[1], c='tab:green')
    # ax2.scatter(x1,aaa[2], c='tab:blue')
    fig.draw()  
        
        

def ran():
    global x
    global y
    y=np.random.randint(0,480)
    x=np.random.randint(0,640)
    
c=Thread(target=ch)


def choose_start():
    print("start")
    c.daemon=True
    c.start()



root = tk.Tk()
root.bind('<Escape>', lambda e: root.quit()) 
figure1 = plt.Figure(figsize=(6, 5), dpi=100)

ax2 = figure1.add_subplot(111)
#ax2.set_ylim(0,255)
fig = FigureCanvasTkAgg(figure1, root)
fig.get_tk_widget().pack(side=tk.LEFT, fill='both')

can= tk.Label()
can.pack(side=tk.RIGHT, fill='both')


b1 = tk.Button(text='color',command=choose_start)
b1.pack(side=tk.RIGHT,anchor='e')

root.bind("<Return>",s)
b1 = tk.Button(text='rand',command=ran)
b1.pack(side=tk.RIGHT,anchor='e')

#root.after(1,s)
root.mainloop()