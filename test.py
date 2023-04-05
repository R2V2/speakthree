from tkinter import *
import tkinter as tk
from dataframepractice import *
TK_SILENCE_DEPRECATION=1

gui = tk.Tk()
gui.title("Abra-Merlin")
gui.geometry("700x700")

masterFrame = tk.Frame(gui)
masterFrame.pack()
frame = tk.Frame(masterFrame)
frame.pack()

df = firstPass(string15)
label = Label(frame, text=df[0],
              cursor="hand2", foreground="green", font=('Helvetica 18'))

def unfold(struct):
    wordsPerLine = 11
    labels = []
    for widgets in masterFrame.winfo_children():
        widgets.destroy()

    words = [x[0] for x in struct]
    words[-1] = words[-1][0]+"."
    frames = [tk.Frame(masterFrame)]
    frames[0].pack()
    nFrames = int(len(words)/ wordsPerLine) + (21 % 5 > 0)
    if nFrames != 1:
        for i in range(0,nFrames):
                frames.append(tk.Frame(masterFrame, pady=-20))
        for f in frames:
            f.pack()

    activeFrame = frames.pop(0)
    counter = 1
    for word in words:
        if counter < wordsPerLine+1:
            labels.append(Label(activeFrame, text=word, cursor="hand2", foreground="green", font=('Helvetica 18')))
            counter += 1
        else:
            labels.append(Label(activeFrame, text=word, cursor="hand2", foreground="green", font=('Helvetica 18')))
            activeFrame = frames.pop(0)
            counter = 1
    
    counter = 1
    for item in labels:
        item.pack(side=LEFT, pady=15)
        item.bind("<Button-1>", lambda e, btn=counter: unfold(move(struct,btn)))
        counter += 1
     

label.pack(side=LEFT, pady=15)
label.bind("<Button-1>", lambda e: unfold(speakThree(df)))
gui.mainloop()
