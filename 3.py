from tkinter import *
 
 
def event_info(event):
    # print(event)
    print(event.char)

 

root = Tk()
root.bind('a', event_info)
root.bind('1', event_info)
root.mainloop()