import os
os.environ["TK_SILENCE_DEPRECATION"] = "1"
import tkinter as tk

PASSWORD = "letmein"   # change this to whatever you want the correct answer to be

root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="black")

title = tk.Label(
    root,
    text="ENTER PASSWORD",
    font=("Helvetica", 40, "bold"),
    fg="#00ff00",
    bg="black",
)
title.place(relx=0.5, rely=0.40, anchor="center")

entry = tk.Entry(
    root,
    font=("Helvetica", 28),
    fg="#00ff00",
    bg="#111111",
    insertbackground="#00ff00",
    justify="center",
    width=30,
    show="*",
)
entry.place(relx=0.5, rely=0.5, anchor="center")
entry.focus_set()

output = tk.Label(
    root,
    text="",
    font=("Helvetica", 28, "bold"),
    fg="#ff3333",
    bg="black",
)
output.place(relx=0.5, rely=0.62, anchor="center")

def on_submit(event=None):
    if entry.get() == PASSWORD:
        root.destroy()
    else:
        output.config(text="ACCESS DENIED")
        entry.delete(0, tk.END)

entry.bind("<Return>", on_submit)
root.bind("<Escape>", lambda e: root.destroy())
root.bind("<Command-q>", lambda e: root.destroy())

root.mainloop()
