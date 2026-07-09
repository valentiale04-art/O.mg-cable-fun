import os
os.environ["TK_SILENCE_DEPRECATION"] = "1"
import tkinter as tk

root = tk.Tk()
root.configure(bg="black")

label = tk.Label(
    root,
    text="🎵 YOU'VE BEEN RICKROLLED 🎵\n\nNever gonna give you up\nNever gonna let you down\n\n[ press ESC to escape ]",
    font=("Helvetica", 48, "bold"),
    fg="#00ff00",
    bg="black",
    justify="center",
)
label.place(relx=0.5, rely=0.5, anchor="center")

root.bind("<Escape>", lambda e: root.destroy())
root.bind("<Command-q>", lambda e: root.destroy())

def go_fullscreen():
    root.overrideredirect(True)
    root.overrideredirect(False)   # toggle resets the mac decoration bug
    root.overrideredirect(True)
    root.attributes("-fullscreen", True)
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
    root.attributes("-topmost", True)
    root.focus_force()

root.after(100, go_fullscreen)   # let the window map first, THEN take over
root.mainloop()
