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

### R
        self.varR = StringVar()
        self.frameR= Frame(self)
        self.frameR.pack()
        self.lblR = tk.Label(self.frameR, text="R")
        self.lblR.pack(side = LEFT, anchor = S)
        self.scaleR = Scale(self.frameR,
        from_=0, to =255,orient = HORIZONTAL, length = 256, command = self.change, variable = self.varR)

        self.scaleR.pack(side = LEFT, anchor = S)
        self.entryR = Entry(self.frameR, width = 5, textvariable = self.varR)
        self.entryR.pack(side = LEFT, anchor = S)
### G
        self.varG = StringVar()
        self.frameG = Frame(self)
        self.frameG.pack()
        self.lblG = tk.Label(self.frameG, text="G")
        self.lblG.pack(side = LEFT, anchor = S)
        self.scaleG = Scale(self.frameG,
        from_=0, to =255,orient = HORIZONTAL, length = 256, command = self.change, variable = self.varG)
        
        self.scaleG.pack(side = LEFT, anchor = S)
        self.entryG = Entry(self.frameG, width = 5,  textvariable = self.varG)
        self.entryG.pack(side = LEFT, anchor = S)
### B
        self.varB = StringVar()
        self.frameB = Frame(self)
        self.frameB.pack()
        self.lblB = tk.Label(self.frameB, text="B")
        self.lblB.pack(side = LEFT, anchor = S)
        self.scaleB = Scale(self.frameB,
        from_=0, to =255,orient = HORIZONTAL, length = 256, command = self.change, variable = self.varB)

        self.scaleB.pack(side = LEFT, anchor = S)
        self.entryB = Entry(self.frameB, width = 5,  textvariable = self.varB)
        self.entryB.pack(side = LEFT, anchor = S)
        
        
        self.canvasMain = Canvas(width = 256, height = 100, background = "#000000")
        self.canvasMain.pack()



        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()

        #self.btn2 = tk.Button(self, text="About", command=self.quit)
        #self.btn2.pack()

    def change(self, event):
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        self.canvasMain.config(background = f"#{r:02x}{g:02x}{b:02x}")


        #self.varR.set(r)
        #self.varG.set(g)
        #self.varB.set(b)



    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
