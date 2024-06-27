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

# vid = imageio.get_reader('<video0>')

import imageio.v3 as iio
vid = iio.imiter("<video1>")
frame=None
a=time.time()
ct=time.time()
fps=0
x=100
y=100
def video_capture():
    global frame
    global a
    global fps
    ct=time.time()
    frame = next(vid) 
    a=time.time()-ct
    captured_image = Image.fromarray(frame) 
    photo_image = ImageTk.PhotoImage(image=captured_image) 
    can.photo_image = photo_image 
    can.configure(image=photo_image)
    root.after(1,video_capture)
    print(a)
    #root.event_generate("<<event>>")



size=20

li=[0]*size
x1=np.arange(size)
def upd_graph(event):
    global fps
    li.append(fps)
    li.pop(0)
    ax2.clear()
    ax2.scatter(x1,li, c='tab:red')
    fig.draw() 



def START_WORK():
    print("start work")
    c1.start()




root = tk.Tk()
figure1 = plt.Figure(figsize=(6, 5), dpi=100)

ax2 = figure1.add_subplot(111)
#ax2.set_ylim(0,255)
fig = FigureCanvasTkAgg(figure1, root)
fig.get_tk_widget().pack(side=tk.LEFT, fill='both')

can= tk.Label(root)
can.pack(side=tk.RIGHT, fill='both')


root.bind("<<event>>",upd_graph)
root.after(1,video_capture)
root.mainloop()

