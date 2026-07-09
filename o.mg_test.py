import tkinter as tk

root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="black")
root.attributes("-topmost", True)

label = tk.Label(
    root,
    text="🎵 YOU'VE BEEN RICKROLLED 🎵\n\nNever gonna give you up\nNever gonna let you down\n\n[ press ESC to escape ]",
    font=("Helvetica", 40, "bold"),
    fg="#00ff00",
    bg="black",
    justify="center",
)
label.place(relx=0.5, rely=0.5, anchor="center")

# ESC closes it; reboot also clears it since nothing persists
root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()
