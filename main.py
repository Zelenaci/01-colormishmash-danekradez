#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import Scale, HORIZONTAL, Canvas
# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "ColorMishMash"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)

        self.bind("<Escape>", self.quit)

        self.lblR = tk.Label(self, text="R")
        self.lblR.pack()
        self.scaleR = Scale(from_=0, to =255,orient = HORIZONTAL, length = 256, command = self.change)
        self.scaleR.pack()

        self.lblG = tk.Label(self, text="G")
        self.lblG.pack()
        self.scaleG = Scale(from_=0, to =255,orient = HORIZONTAL, length = 256, command = self.change)
        self.scaleG.pack()

        self.lblB = tk.Label(self, text="B")
        self.lblB.pack()
        self.scaleB = Scale(from_=0, to =255,orient = HORIZONTAL, length = 256, command = self.change)
        self.scaleB.pack()

        self.canvasMain = Canvas(width = 256, height = 100, background = "#987654")
        self.canvasMain.pack()



        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()

        self.btn2 = tk.Button(self, text="About", command=self.quit)
        self.btn2.pack()

        def change(self, event):
            self.lblG.config(text = "nigga")
            self.canvasMain.config(background = "#562398")
        
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        self.canvasMain.config(background = f"{r:02x}{g:02x}{b:02x}")
        print(f"{r:2x}{g:2x}{b:2x}")
        print(f"{r:02x}{g:02x}{b:02x}")



    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
