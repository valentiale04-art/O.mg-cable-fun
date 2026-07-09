import os
os.environ["TK_SILENCE_DEPRECATION"] = "1"
import tkinter as tk

PASSWORD = "admin"

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
    show="•",
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

def
