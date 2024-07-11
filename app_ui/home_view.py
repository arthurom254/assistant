import tkinter as tk
from tkinter import messagebox
import time
def record(): 
    canvas.itemconfig(button_text, text="Listening...")
    time.sleep(4)

root = tk.Tk()
root.title("AI powered Virtual Assistant")
root.geometry("300x300")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

def create_circle(x, y, r, canvas, **kwargs):
    return canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

button = create_circle(150, 150, 50, canvas, fill="blue", outline="blue")

button_text = canvas.create_text(150, 150, text="Click to Speak", fill="white", font=("Helvetica", 12, "bold"))

def on_button_click(event):
    record()

canvas.tag_bind(button, "<Button-1>", on_button_click)
canvas.tag_bind(button_text, "<Button-1>", on_button_click)

root.mainloop()
