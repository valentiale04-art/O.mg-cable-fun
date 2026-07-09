import os
import tkinter as tk
import Quartz  # pip install pyobjc-framework-Quartz

os.environ["TK_SILENCE_DEPRECATION"] = "1"

PASSWORD = "letmein"   # change this to whatever you want the correct answer to be

root = tk.Tk()

# --- Cover the whole screen WITHOUT macOS native fullscreen (avoids grey screen) ---
SCREEN_W = root.winfo_screenwidth()
SCREEN_H = root.winfo_screenheight()
root.overrideredirect(True)                         # borderless window
root.geometry(f"{SCREEN_W}x{SCREEN_H}+0+0")         # cover entire screen
root.attributes("-topmost", True)                   # stay on top
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
    insertbackground="#00ff00",   # cursor color
    justify="center",
    width=30,
    show="*",                     # masks input like a real password field
)
entry.place(relx=0.5, rely=0.5, anchor="center")

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

# --- mouse border: keep cursor 1 inch inside every screen edge ---
MARGIN = int(root.winfo_fpixels("1i"))   # pixels in 1 inch
LEFT, TOP = MARGIN, MARGIN
RIGHT, BOTTOM = SCREEN_W - MARGIN, SCREEN_H - MARGIN

def clamp_mouse():
    loc = Quartz.CGEventGetLocation(Quartz.CGEventCreate(None))
    x, y = loc.x, loc.y
    cx = min(max(x, LEFT), RIGHT)
    cy = min(max(y, TOP), BOTTOM)
    if (cx, cy) != (x, y):
        Quartz.CGWarpMouseCursorPosition((cx, cy))
        Quartz.CGAssociateMouseAndMouseCursorPosition(True)
    root.after(10, clamp_mouse)

# make sure the window is drawn and focused before we start
root.update()
root.lift()
root.focus_force()
entry.focus_set()

clamp_mouse()
root.mainloop()
