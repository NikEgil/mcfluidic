import tkinter as tk

class MoveRectangles():
    def __init__(self, root):
        self.root=root
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.grid()

        # canvas.create_rectangle(x0, y0, x1, y1, option, ... )
        # x0, y0, x1, y1 are corner coordinates of ulc to lrc diagonal
        self.rc1 = self.canvas.create_rectangle(20, 260, 120, 360,
                          outline='white', fill='blue')
        self.rc2 = self.canvas.create_rectangle(20, 10, 120, 110,
                          outline='white', fill='red')

        self.max_moves=50
        self.move_rectangle()

    def move_rectangle(self):
        y = x = 5
        if self.max_moves:
            self.canvas.move(self.rc1, x, -y)
            self.canvas.move(self.rc2, x, y)
            self.max_moves -= 1
            self.canvas.after(100, self.move_rectangle)
        else:
            self.root.quit()

root = tk.Tk()
MR=MoveRectangles(root)
root.mainloop()