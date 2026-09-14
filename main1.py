import tkinter as tk
from tkinter import ttk


def show_message():
    hours = float(entry.get())

    progress_bar["value"] = min(hours, 3)

    if hours >= 3:
        status.config(text="Daily target completed! 🔥")
    elif hours >= 1.5:
        status.config(text="Good progress! 💪")
    else:
        status.config(text="Keep going! 🚀")


window = tk.Tk()
window.title("AI Journey Dashboard")
window.geometry("500x400")

title = tk.Label(
    window,
    text="AI ENGINEER JOURNEY",
    font=("Arial", 24)
)
title.pack(pady=30)

label = tk.Label(
    window,
    text="How many hours did you study today?",
    font=("Arial", 14)
)
label.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=10)

button = tk.Button(
    window,
    text="Update Progress",
    command=show_message,
    font=("Arial", 12)
)
button.pack(pady=15)

progress_bar = ttk.Progressbar(
    window,
    length=300,
    maximum=3
)
progress_bar.pack(pady=15)

status = tk.Label(
    window,
    text="Enter your study hours",
    font=("Arial", 14)
)
status.pack(pady=15)

window.mainloop()