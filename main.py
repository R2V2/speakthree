from tkinter import *
import tkinter as tk
from dataframe import *
TK_SILENCE_DEPRECATION=1

gui = tk.Tk()
gui.title("Abra-Merlin")
gui.geometry("700x700")

masterFrame = tk.Frame(gui)
masterFrame.pack()
frame = tk.Frame(masterFrame)
frame.pack()

df = firstPass(string31)
label = Label(frame, text=df[0],
              cursor="sb_h_double_arrow", foreground="white", font=('Helvetica 18'))

def unfold(struct):
    wordsPerLine = 11
    labels = []
    for widgets in masterFrame.winfo_children():
        widgets.destroy()

    words = [x[0] for x in struct]
    #capitalize the first word in list
    if type(words[0])==list:
         words[0] = words[0][0].capitalize()
    else:
         words[0] = words[0].capitalize()
    #add period to last word in list
    if type(words[-1])==list:
         words[-1] = words[-1][0]+"."
    else:
         words[-1] = words[-1]+"."

    #create new frames based on number of words
    frames = [tk.Frame(masterFrame)]
    frames[0].pack()
    nFrames = int(len(words)/ wordsPerLine) + (21 % 5 > 0)
    if nFrames != 1:
        for i in range(0,nFrames):
                frames.append(tk.Frame(masterFrame))
        for f in frames:
            f.pack()

    #create labels in frames
    activeFrame = frames.pop(0)
    counter = 1
    for word in words:
        if counter < wordsPerLine+1:
            labels.append(Label(activeFrame, text=word, cursor="circle", foreground="black", font=('Helvetica 18')))
            counter += 1
        else:
            labels.append(Label(activeFrame, text=word, cursor="circle", foreground="black", font=('Helvetica 18')))
            activeFrame = frames.pop(0)
            counter = 1
    
    #loop through labels and pack them into frames, then bind the proper command for it to call
    counter = 1
    for item in labels:
        item.pack(side=LEFT, pady=15)
        item.bind("<Button-1>", lambda e, btn=counter: unfold(move(struct,btn)))
        counter += 1
     

label.pack(side=LEFT, pady=15)
label.bind("<Button-1>", lambda e: unfold(abra(df)))
gui.mainloop()
