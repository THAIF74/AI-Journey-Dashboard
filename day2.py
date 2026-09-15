import tkinter as tk
from tkinter import ttk

# ---------------- WINDOW ----------------

window = tk.Tk()
window.title("AI Journey Dashboard")
window.geometry("750x500")
window.configure(bg="#0f172a")

# ---------------- COLORS ----------------

BG = "#0f172a"
CARD = "#1e293b"
ACCENT = "#38bdf8"
TEXT = "#f8fafc"
SECONDARY = "#94a3b8"
BUTTON = "#334155"
HOVER = "#475569"

# ---------------- TITLE ----------------

title = tk.Label(
    window,
    text="AI JOURNEY DASHBOARD",
    font=("Arial", 26, "bold"),
    bg=BG,
    fg=ACCENT
)
title.pack(pady=(30, 10))

subtitle = tk.Label(
    window,
    text="Building myself into an AI Engineer",
    font=("Arial", 13),
    bg=BG,
    fg=SECONDARY
)
subtitle.pack(pady=(0, 20))

# ---------------- INFO ----------------

info_frame = tk.Frame(
    window,
    bg=CARD
)
info_frame.pack(pady=5, padx=30, fill="x")

goal = tk.Label(
    info_frame,
    text="Goal: AI Engineer",
    font=("Arial", 14, "bold"),
    bg=CARD,
    fg=TEXT
)
goal.pack(side="left", padx=30, pady=15)

stage = tk.Label(
    info_frame,
    text="Stage: Python Fundamentals",
    font=("Arial", 14),
    bg=CARD,
    fg=SECONDARY
)
stage.pack(side="right", padx=30, pady=15)

# ---------------- PROGRESS ----------------

progress_label = tk.Label(
    window,
    text="Today's Study Progress",
    font=("Arial", 14, "bold"),
    bg=BG,
    fg=TEXT
)
progress_label.pack(pady=(25, 5))

progress_bar = ttk.Progressbar(
    window,
    length=500,
    maximum=3
)
progress_bar.pack(pady=5)

# ---------------- PROGRESS FUNCTION ----------------

def show_progress():
    hours = float(entry.get())
    progress_bar["value"] = min(hours, 3)

    if hours >= 3:
        message.config(
            text="Daily target completed! 🔥",
            fg=ACCENT
        )
    elif hours >= 1.5:
        message.config(
            text="Good progress! 💪",
            fg=TEXT
        )
    else:
        message.config(
            text="Keep going! 🚀",
            fg=SECONDARY
        )

# ---------------- HOURS ENTRY ----------------

entry = tk.Entry(
    window,
    font=("Arial", 13),
    bg=CARD,
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat",
    width=20
)
entry.pack(pady=10)

button = tk.Button(
    window,
    text="Check My Progress",
    command=show_progress,
    font=("Arial", 11, "bold"),
    bg=ACCENT,
    fg=BG,
    activebackground=ACCENT,
    relief="flat",
    padx=15,
    pady=8
)
button.pack(pady=5)

message = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    bg=BG
)
message.pack(pady=8)

# ---------------- MENU ----------------

menu = tk.Frame(
    window,
    bg=BG
)
menu.pack(pady=15)

# ---------------- LEARNING ----------------

def show_learning():
    learning_window = tk.Toplevel(window)
    learning_window.title("Learning")
    learning_window.geometry("400x300")
    learning_window.configure(bg=BG)

    title = tk.Label(
        learning_window,
        text="MY LEARNING",
        font=("Arial", 20, "bold"),
        bg=BG,
        fg=ACCENT
    )
    title.pack(pady=25)

    topic = tk.Label(
        learning_window,
        text="Current: Python Fundamentals",
        font=("Arial", 14),
        bg=BG,
        fg=TEXT
    )
    topic.pack(pady=10)


learning_button = tk.Button(
    menu,
    text="Learning",
    command=show_learning,
    font=("Arial", 10, "bold"),
    bg=BUTTON,
    fg=TEXT,
    activebackground=HOVER,
    activeforeground=TEXT,
    relief="flat",
    padx=12,
    pady=8
)
learning_button.pack(side="left", padx=5)

# ---------------- PROJECTS ----------------

def show_projects():
    projects_window = tk.Toplevel(window)
    projects_window.title("Projects")
    projects_window.geometry("450x300")
    projects_window.configure(bg=BG)

    title = tk.Label(
        projects_window,
        text="MY PROJECTS",
        font=("Arial", 20, "bold"),
        bg=BG,
        fg=ACCENT
    )
    title.pack(pady=25)

    project = tk.Label(
        projects_window,
        text="Project 1: AI Journey Dashboard",
        font=("Arial", 14),
        bg=BG,
        fg=TEXT
    )
    project.pack(pady=10)

    status = tk.Label(
        projects_window,
        text="Status: In Progress",
        font=("Arial", 14),
        bg=BG,
        fg=SECONDARY
    )
    status.pack(pady=10)


projects_button = tk.Button(
    menu,
    text="Projects",
    command=show_projects,
    font=("Arial", 10, "bold"),
    bg=BUTTON,
    fg=TEXT,
    activebackground=HOVER,
    activeforeground=TEXT,
    relief="flat",
    padx=12,
    pady=8
)
projects_button.pack(side="left", padx=5)

# ---------------- CAREER ----------------

def show_career():
    career_window = tk.Toplevel(window)
    career_window.title("Career")
    career_window.geometry("450x300")
    career_window.configure(bg=BG)

    title = tk.Label(
        career_window,
        text="MY CAREER",
        font=("Arial", 20, "bold"),
        bg=BG,
        fg=ACCENT
    )
    title.pack(pady=25)

    goal = tk.Label(
        career_window,
        text="Target: AI Engineer",
        font=("Arial", 14),
        bg=BG,
        fg=TEXT
    )
    goal.pack(pady=10)

    internship = tk.Label(
        career_window,
        text="Internships: To be started",
        font=("Arial", 14),
        bg=BG,
        fg=SECONDARY
    )
    internship.pack(pady=10)

    skills = tk.Label(
        career_window,
        text="Skills: Python → DSA → ML → AI",
        font=("Arial", 14),
        bg=BG,
        fg=TEXT
    )
    skills.pack(pady=10)


career_button = tk.Button(
    menu,
    text="Career",
    command=show_career,
    font=("Arial", 10, "bold"),
    bg=BUTTON,
    fg=TEXT,
    activebackground=HOVER,
    activeforeground=TEXT,
    relief="flat",
    padx=12,
    pady=8
)
career_button.pack(side="left", padx=5)

# ---------------- IDEAS ----------------

def show_ideas():
    ideas_window = tk.Toplevel(window)
    ideas_window.title("Ideas Vault")
    ideas_window.geometry("450x300")
    ideas_window.configure(bg=BG)

    title = tk.Label(
        ideas_window,
        text="MY AI IDEAS",
        font=("Arial", 20, "bold"),
        bg=BG,
        fg=ACCENT
    )
    title.pack(pady=25)

    idea = tk.Label(
        ideas_window,
        text="Store future AI product ideas here.",
        font=("Arial", 14),
        bg=BG,
        fg=TEXT
    )
    idea.pack(pady=10)

    example = tk.Label(
        ideas_window,
        text="Example: Personal AI Study Assistant",
        font=("Arial", 12),
        bg=BG,
        fg=SECONDARY
    )
    example.pack(pady=10)


ideas_button = tk.Button(
    menu,
    text="Ideas",
    command=show_ideas,
    font=("Arial", 10, "bold"),
    bg=BUTTON,
    fg=TEXT,
    activebackground=HOVER,
    activeforeground=TEXT,
    relief="flat",
    padx=12,
    pady=8
)
ideas_button.pack(side="left", padx=5)

# ---------------- DAILY TRACKER ----------------

def show_tracker():
    tracker_window = tk.Toplevel(window)
    tracker_window.title("Daily Tracker")
    tracker_window.geometry("450x350")
    tracker_window.configure(bg=BG)

    title = tk.Label(
        tracker_window,
        text="DAILY TRACKER",
        font=("Arial", 20, "bold"),
        bg=BG,
        fg=ACCENT
    )
    title.pack(pady=25)

    study = tk.Label(
        tracker_window,
        text="Study: Python Fundamentals",
        font=("Arial", 14),
        bg=BG,
        fg=TEXT
    )
    study.pack(pady=10)

    coding = tk.Label(
        tracker_window,
        text="Coding: Completed",
        font=("Arial", 14),
        bg=BG,
        fg=SECONDARY
    )
    coding.pack(pady=10)

    project = tk.Label(
        tracker_window,
        text="Project: AI Journey Dashboard",
        font=("Arial", 14),
        bg=BG,
        fg=TEXT
    )
    project.pack(pady=10)

    progress = tk.Label(
        tracker_window,
        text="Day 2 Progress: 🔥",
        font=("Arial", 14),
        bg=BG,
        fg=ACCENT
    )
    progress.pack(pady=10)


tracker_button = tk.Button(
    menu,
    text="Daily Tracker",
    command=show_tracker,
    font=("Arial", 10, "bold"),
    bg=BUTTON,
    fg=TEXT,
    activebackground=HOVER,
    activeforeground=TEXT,
    relief="flat",
    padx=12,
    pady=8
)
tracker_button.pack(side="left", padx=5)

# ---------------- START ----------------

window.mainloop()