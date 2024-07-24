import tkinter as tk

root = tk.Tk()
root.title("AI Powered Virtual Assistant")
root.geometry("300x300")

progress_label = tk.Label(root, text="Waiting for action", font=("Helvetica", 12), justify="center")
progress_label.pack()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

def create_circle(x, y, r, canvas, **kwargs):
    return canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

button = create_circle(150, 100, 50, canvas, fill="teal", outline="tan")
button_text = canvas.create_text(150, 100, text="Click to Speak", fill="white", activefill='tan', font=("Helvetica", 10, "bold"))

def on_button_click(event):
    from nlp.speech_to_text import speechToText
    from ai_engine.main import aiEngine
    text = speechToText()
    
    if text != 0:
        if "generate" in text and "image" in text:
            from nlp.text_to_speech import speakAloud
            speakAloud(text)
            from img import img_gen
            img_gen(text)
        else:
            aiEngine(text)
        update_progress_text("Press the button to start microphone")


canvas.tag_bind(button, "<Button-1>", on_button_click)
canvas.tag_bind(button_text, "<Button-1>", on_button_click)

def update_progress_text(new_text):
    global progress_label
    progress_label.config(text=new_text)

def update_button_text(new_text):
    canvas.itemconfig(button_text, text=new_text)

if __name__ == "__main__":
    root.mainloop()
