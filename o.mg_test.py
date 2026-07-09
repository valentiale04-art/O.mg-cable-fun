import os
os.environ["TK_SILENCE_DEPRECATION"] = "1"
import tkinter as tk

PASSWORD = "admin"   # <-- change this to whatever you want

root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="black")

# --- Title text ---
title = tk.Label(
    root,
    text="ENTER PASSWORD",
    font=("Helvetica", 40, "bold"),
    fg="#00ff00",
    bg="black",
)
title.place(relx=0.5, rely=0.40, anchor="center")

# --- The typing bar (input) ---
entry = tk.Entry(
    root,
    font=("Helvetica", 28),
    fg="#00ff00",
    bg="#111111",
    insertbackground="#00ff00",   # cursor color
    justify="center",
    width=30,
    show="•",                     # masks input like a real password field
)
entry.place(relx=0.5, rely=0.5, anchor="center")
entry.focus_set()

# --- Feedback line (for wrong answers) ---
output = tk.Label(
    root,
    text="",
    font=("Helvetica", 28, "bold"),
    fg="#ff3333",
    bg="black",
)
output.place(relx=0.5,
