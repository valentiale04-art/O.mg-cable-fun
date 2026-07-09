import os
os.environ["TK_SILENCE_DEPRECATION"] = "1"
import tkinter as tk

root = tk.Tk()
root.configure(bg="black")
root.update_idletasks()

sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{sw}x{sh}+0+0")
root.update()

label = tk.Label(root, text="🎵 YOU'VE BEEN RICKROLLED 🎵\n\nNever gonna give you up\nNever gonna let
