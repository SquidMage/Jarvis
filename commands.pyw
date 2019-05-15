#! python3

# commands.pyw - A module of functions for jarvis.pyw

import webbrowser
from tkinter import *
from subprocess import call

# Compares the user input to known commands.
def checkInput(command):

    # Sperates the arguments into a list.
    arguments = command.split(" ")
    print(arguments)
    key = arguments[0]
    arguments.remove(key)

    # Checks for and calls mail().
    if key.lower() == "mail":
        mail()

    # Checks for and calls wetter().
    elif key.lower() == "wetter":
        if len(arguments) == 0:
            wetter()
        else:
            place = " ".join(arguments)
            wetter(place)

    # Checks for and calls net().        
    elif key.lower() == "net":
        net()

    # Checks for and calls search().
    elif key.lower() == "search":
        if len(arguments) == 0:
            print("No keywords were given.")
        else:
            "+".join(arguments)
            search(arguments)
    # Checks for and calls help().
    elif key.lower() == "help":
        getHelp()

def mail():
    webbrowser.open(r"https://mail.google.com/mail/u/0/#inbox")
    webbrowser.open(r"https://mail.google.com/mail/u/1/#inbox")
    webbrowser.open(r"https://mail.google.com/mail/u/2/#inbox")

def net():
    webbrowser.open(r"www.google.com")

def wetter(place = ""):
    webbrowser.open(r"https://www.google.com/search?q=wetter" + "+" + place)

def search(txt):
    webbrowser.open(r"https://www.google.com/search?q=" + txt)
    

def getHelp():
    info = Tk()
    info.wm_title("Help")
    
    labelMail = Label(info, text="mail: Opens all three of my gmail accounts.")
    labelMail.pack()
    labelNet = Label(info, text="net: Opens a new tab in my standard webbrowser.")
    labelNet.pack()
    labelWetter = Label(info, text="wetter (+ optional argument): Opens information about the weather at default or specified location.")
    labelWetter.pack()
    labelSearch = Label(info, text="search + keywords: Searches the given keywords on google.")
    labelSearch.pack()


