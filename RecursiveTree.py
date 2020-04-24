#15.31 Recursive tree
from tkinter import *

class RecursiveTree:
    def __init__(self):
        window = Tk()
        window.title("Recursive Tree")

        self.width = 200
        self.height = 200
        self.canvas = Canvas(window, width = self.width,
                             height = self.height)
        self.canvas.pack()

        frame1 = Frame(window)
        frame1.pack()

        Label(frame1, text = "Enter the depth").pack(side = LEFT)
        self.depth = StringVar()
        Entry(frame1, textvariable = self.depth,
              justify = RIGHT).pack(side = LEFT)
        Button(frame1, text = "Display",
               command = self.display).pack(side = LEFT)

        window.mainloop()

    
    def display(self):
        self.canvas.delete("line")
        p1 = [self.width / 2, self.height]
        p2 = [self.width / 2, 2 * self.height / 3]
        size = self.height / 3
        self.displayLine(int(self.depth.get()), p1, p2, size)

    def displayLine(self, depth, p1, p2, size):
        self.drawLine(p1, p2)

        if depth > 0:
            p5 = 2 * [0]
            p3 = 2 * [0]
            p4 = 2 * [0]
            p5[0] = 1.5 * p2[0] - 0.5 * p1[0]
            p5[1] = 1.5 * p2[1] - 0.5 * p1[1]

            p3[0] = (p2[0] + p5[0] + 1.73205 * (p2[1] - p5[1]))/2
            p3[1] = (p2[1] + p5[1] + 1.73205 * (p2[0] - p5[0]))/2
            
            p4[0] = (p2[0] + p5[0] - 1.73205 * (p2[1] - p5[1]))/2
            p4[1] = (p2[1] + p5[1] - 1.73205 * (p2[0] - p5[0]))/2
            
            self.displayLine(depth - 1, p2, p3, size / 2)
            self.displayLine(depth - 1, p2, p4, size / 2)

    def drawLine(self, p1, p2):
        self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], tags = "line")

RecursiveTree()
