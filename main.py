#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import Scale, HORIZONTAL, Canvas, Frame, Entry, LEFT, S, StringVar
# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "ColorMishMash"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)

        self.bind("<Escape>", self.quit)

# R
        self.varR = StringVar()
        self.frameR = Frame(self)
        self.frameR.pack()
        self.lblR = tk.Label(self.frameR, text="R")
        self.lblR.pack(side=LEFT, anchor=S)
        self.scaleR = Scale(self.frameR,
                            from_=0, to=255, orient=HORIZONTAL, length=256, variable=self.varR)

        self.scaleR.pack(side=LEFT, anchor=S)
        self.entryR = Entry(self.frameR, width=5, textvariable=self.varR)
        self.entryR.pack(side=LEFT, anchor=S)
# G
        self.varG = StringVar()
        self.frameG = Frame(self)
        self.frameG.pack()
        self.lblG = tk.Label(self.frameG, text="G")
        self.lblG.pack(side=LEFT, anchor=S)
        self.scaleG = Scale(self.frameG,
                            from_=0, to=255, orient=HORIZONTAL, length=256, variable=self.varG)

        self.scaleG.pack(side=LEFT, anchor=S)
        self.entryG = Entry(self.frameG, width=5,  textvariable=self.varG)
        self.entryG.pack(side=LEFT, anchor=S)
# B
        self.varB = StringVar()
        self.frameB = Frame(self)
        self.frameB.pack()
        self.lblB = tk.Label(self.frameB, text="B")
        self.lblB.pack(side=LEFT, anchor=S)
        self.scaleB = Scale(self.frameB,
                            from_=0, to=255, orient=HORIZONTAL, length=256, variable=self.varB)

        self.scaleB.pack(side=LEFT, anchor=S)
        self.entryB = Entry(self.frameB, width=5,  textvariable=self.varB)
        self.entryB.pack(side=LEFT, anchor=S)

        self.canvasMain = Canvas(width=256, height=100, background="#000000")
        self.canvasMain.pack()
        self.canvasMain.bind("<Button-1>", self.mousehandler)

        self.varMain = StringVar()
        self.entryMain = Entry(self,
                               textvariable=self.varMain,
                               state="readonly",
                               readonlybackground="#f3f3f3")
        self.entryMain.pack()

        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()

        #self.btn2 = tk.Button(self, text="About", command=self.quit)
        # self.btn2.pack()

        self.varR.trace("w", self.change)
        self.varG.trace("w", self.change)
        self.varB.trace("w", self.change)

        self.frameMem = Frame(self)
        self.frameMem.pack()
        self.canvasMem = []
        for row in range(3):
                for column in range(7):
                        canvas = Canvas(self.frameMem, width=50, height=50, background="#abcdef")
                        canvas.grid(row = row, column = column)
                        canvas.bind("<Button-1>", self.mousehandler)
                        self.canvasMem.append(canvas)



    def mousehandler(self, event):
            #print(dir(event))
            if self.cget("cursor") !="pencil":
                    self.config(cursor="pencil")
                    self.color = event.widget.cget("background")
            elif self.cget("cursor") == "pencil":
                    self.config(cursor ="")
                    event.widget.config(background =  self.color)


    def change(self, var, index, mode):
        r = int(self.varR.get())
        g = int(self.varG.get())
        b = int(self.varB.get())
        colorstring = f"#{r:02X}{g:02X}{b:02X}"
        self.canvasMain.config(background=colorstring)
        self.varMain.set(colorstring)

        # self.varR.set(r)
        # self.varG.set(g)
        # self.varB.set(b)
        #r = self.scaleR.get()
        #g = self.scaleG.get()
        #b = self.scaleB.get()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
