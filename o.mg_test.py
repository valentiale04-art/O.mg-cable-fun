import os
os.environ["TK_SILENCE_DEPRECATION"] = "1"
import tkinter as tk

root = tk.Tk()
root.configure(bg="black")

# Force the window to exist and render BEFORE going fullscreen/topmost
root.update_idletasks()
root.deiconify()

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

# Draw first, THEN apply fullscreen + focus — order matters on macOS
root.update()
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.update()
root.focus_force()
root.lift()

root.mainloop()
