import tkinter as tk

root = tk.Tk()

# Kill window decorations and force it over everything (menu bar, Dock)
root.overrideredirect(True)
root.attributes("-topmost", True)

# Size it to the full screen dimensions explicitly
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
root.geometry(f"{screen_w}x{screen_h}+0+0")

root.configure(bg="black")

# macOS-specific: this is what actually forces true fullscreen coverage
try:
    root.attributes("-fullscreen", True)
except tk.TclError:
    pass

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

# Grab focus so keystrokes (ESC) reliably reach the window
root.focus_force()

root.mainloop()
