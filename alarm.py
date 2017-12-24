import pyglet
import time
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Alarm")

def Set():
    Alarm = entry.get()
    Current = time.strftime("%H:%M")

    while Alarm != Current:
        Current = time.strftime("%H:%M")
        time.sleep(1)
    if Alarm == Current:
        song = pyglet.media.load('alarm.mp3')
        song.play()
        pyglet.app.run()

frame = ttk.Frame(root)
frame.pack()
frame.config(height=200, width=200)

label = ttk.Label(frame, text="Alarm Clock :")
label.pack()

entry = ttk.Entry(frame, width=50)
entry.pack()
entry.insert(3, "19:05")


button = ttk.Button(frame, text="Set Alarm", command=Set)
button.pack()

root.mainloop()


