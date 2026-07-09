import os
import sys
import ctypes
import tkinter as tk

os.environ["TK_SILENCE_DEPRECATION"] = "1"

PASSWORD = "letmein"   # change this to whatever you want the correct answer to be

# ---------------------------------------------------------------------------
# Platform detection for the mouse wall
# ---------------------------------------------------------------------------
IS_WINDOWS = sys.platform.startswith("win")
IS_MAC = sys.platform == "darwin"

user32 = ctypes.windll.user32 if IS_WINDOWS else None

HAVE_QUARTZ = False
if IS_MAC:
    try:
        import Quartz  # pip install pyobjc-framework-Quartz
        HAVE_QUARTZ = True
    except ImportError:
        HAVE_QUARTZ = False

if IS_WINDOWS:
    class RECT(ctypes.Structure):
        _fields_ = [("left", ctypes.c_long),
                    ("top", ctypes.c_long),
                    ("right", ctypes.c_long),
                    ("bottom", ctypes.c_long)]
    try:
        user32.SetProcessDPIAware()  # so pixel coords aren't virtualized
    except Exception:
        pass

# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------
# Mouse wall: keep cursor 1 inch inside every edge of the screen
# ---------------------------------------------------------------------------
# winfo_fpixels('1i') returns pixels-per-inch, cross-platform.
MARGIN = int(root.winfo_fpixels("1i"))
SCREEN_W = root.winfo_screenwidth()
SCREEN_H = root.winfo_screenheight()

LEFT, TOP = MARGIN, MARGIN
RIGHT, BOTTOM = SCREEN_W - MARGIN, SCREEN_H - MARGIN

_wall_running = True


def enforce_wall_windows():
    if not _wall_running:
        return
    rect = RECT(LEFT, TOP, RIGHT, BOTTOM)
    # Re-apply constantly: alt-tab, focus changes, popups etc. reset the clip.
    user32.ClipCursor(ctypes.byref(rect))
    root.after(100, enforce_wall_windows)


def enforce_wall_mac():
    if not _wall_running:
        return
    loc = Quartz.CGEventGetLocation(Quartz.CGEventCreate(None))
    x, y = loc.x, loc.y
    cx = min(max(x, LEFT), RIGHT)
    cy = min(max(y, TOP), BOTTOM)
    if cx != x or cy != y:
        Quartz.CGWarpMouseCursorPosition((cx, cy))
        # Re-associate immediately so the edge doesn't feel "sticky".
        Quartz.CGAssociateMouseAndMouseCursorPosition(True)
    root.after(8, enforce_wall_mac)


def start_wall():
    if IS_WINDOWS:
        enforce_wall_windows()
    elif IS_MAC and HAVE_QUARTZ:
        enforce_wall_mac()
    else:
        # No supported method (e.g. Linux, or Quartz missing) -> skip the wall.
        print("Mouse wall not available on this setup; running without it.")


def release_wall():
    global _wall_running
    _wall_running = False
    if IS_WINDOWS:
        user32.ClipCursor(None)  # let the mouse roam free again


# ---------------------------------------------------------------------------
# Handlers
# ---------------------------------------------------------------------------
def quit_app(event=None):
    release_wall()
    root.destroy()


def on_submit(event=None):
    if entry.get() == PASSWORD:
        quit_app()
    else:
        output.config(text="ACCESS DENIED")
        entry.delete(0, tk.END)


entry.bind("<Return>", on_submit)
root.bind("<Escape>", quit_app)         # keyboard escape hatch (mouse-proof)
root.bind("<Command-q>", quit_app)      # macOS escape hatch

start_wall()
root.mainloop()

# Safety net in case mainloop exits some other way.
release_wall()
