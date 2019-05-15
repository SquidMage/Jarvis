#! python3

# jarvis.py - My personal helper

import commands, logging
from tkinter import *

class App:

    def __init__(self, master):

        # Creates a frame for the widgets.
        frame = Frame(master, borderwidth=5, width=500, height=200)
        frame.pack(fill=X)

        # Label for the name of the assistant.
        self.label = Label(frame, text="Jarvis", fg="grey", font=("Arial Bold", 35))
        self.label.pack(fill=X)

        # Message from the assistant.
        self.message = Message(frame, text="Hello, how may I help you today?", anchor=CENTER, width=400)
        self.message.pack(fill=X)

        # Binds events to the entry/input widget.
        self.entry = Entry(frame, fg="grey")
        self.entry.insert(0, "Enter your command...")
        self.entry.bind("<FocusIn>", self.onEntryClick)
        self.entry.bind("<Return>", self.onFocusOut)
        self.entry.bind("<Return>", self.getInput)
        self.entry.pack(fill=X)

    # Deletes the standard text when the entry widget is clicked.
    def onEntryClick(self, event):
        if self.entry.get() == "Enter your command...":
            self.entry.delete(0, "end")
            self.entry.insert(0, "")
            self.entry.config(fg="black")

    # Supposed to set entry widget to starting style, need to fix.
    def onFocusOut(self, event):
        if  self.entry.get() != "Enter your command...":
            self.entry.insert(0, "Enter your command...")
            self.entry.config(fg="grey")

    # Gets user input.
    def getInput(self, event):
        self.input = self.entry.get()
        print(self.input)
        commands.checkInput(self.input)
        
root = Tk()
root.geometry("300x150+950+490")
root.title("J.A.R.V.I.S.")
root.x = 2000
root.y = 0

app = App(root)

root.mainloop()
