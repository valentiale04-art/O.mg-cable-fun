import os
os.environ["TK_SILENCE_DEPRECATION"] = "1"
import tkinter as tk

root = tk.Tk()
root.update()

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

# Frameless, no title bar, no dragging — covers menu bar + Dock
root.overrideredirect(True)
root.geometry("%dx%d+0+0" % (sw, sh))
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

root.update()
root.attributes("-topmost", True)
root.lift()
root.focus_force()

root.mainloop()
