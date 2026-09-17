import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import date


# =========================================================
# DATABASE
# =========================================================

connection = sqlite3.connect("ai_journey.db")
cursor = connection.cursor()

# Learning table
cursor.execute("""
CREATE TABLE IF NOT EXISTS learning (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT
)
""")

# Projects table
cursor.execute("""
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    status TEXT
)
""")

# Ideas table
cursor.execute("""
CREATE TABLE IF NOT EXISTS ideas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idea TEXT
)
""")

# Daily Tracker table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tracker (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT UNIQUE,
    hours REAL
)
""")

connection.commit()


# =========================================================
# MAIN WINDOW
# =========================================================

window = tk.Tk()
window.title("AI Journey Dashboard")
window.geometry("750x550")
window.configure(bg="#0f172a")


# =========================================================
# COLORS
# =========================================================

BG = "#0f172a"
CARD = "#1e293b"
ACCENT = "#38bdf8"
TEXT = "#f8fafc"
SECONDARY = "#94a3b8"
BUTTON = "#334155"
HOVER = "#475569"


# =========================================================
# TITLE
# =========================================================

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


# =========================================================
# INFO
# =========================================================

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


# =========================================================
# PROGRESS
# =========================================================

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


# =========================================================
# PROGRESS FUNCTION
# =========================================================

def show_progress():

    try:
        hours = float(entry.get())
    except ValueError:
        message.config(
            text="Please enter a valid number.",
            fg=ACCENT
        )
        return

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


# =========================================================
# HOURS ENTRY
# =========================================================

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
    bg=BG,
    fg=SECONDARY
)
message.pack(pady=8)


# =========================================================
# MENU
# =========================================================

menu = tk.Frame(
    window,
    bg=BG
)
menu.pack(pady=15)


# =========================================================
# LEARNING
# =========================================================

def show_learning():

    learning_window = tk.Toplevel(window)
    learning_window.title("Learning")
    learning_window.geometry("450x350")
    learning_window.configure(bg=BG)

    title = tk.Label(
        learning_window,
        text="MY LEARNING",
        font=("Arial", 20, "bold"),
        bg=BG,
        fg=ACCENT
    )
    title.pack(pady=25)

    topic_label = tk.Label(
        learning_window,
        text="Enter your current topic:",
        font=("Arial", 14),
        bg=BG,
        fg=TEXT
    )
    topic_label.pack(pady=10)

    topic_entry = tk.Entry(
        learning_window,
        font=("Arial", 14),
        bg=CARD,
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat"
    )
    topic_entry.pack(pady=10)

    # Get latest saved topic
    cursor.execute(
        "SELECT topic FROM learning ORDER BY id DESC LIMIT 1"
    )

    saved_topic = cursor.fetchone()

    if saved_topic:
        current_topic = saved_topic[0]
    else:
        current_topic = "Python Fundamentals"

    result = tk.Label(
        learning_window,
        text="Current: " + current_topic,
        font=("Arial", 14),
        bg=BG,
        fg=SECONDARY
    )
    result.pack(pady=10)

    # SAVE TOPIC
    def save_topic():

        topic = topic_entry.get().strip()

        if topic == "":
            result.config(
                text="Please enter a topic.",
                fg=ACCENT
            )
            return

        cursor.execute(
            "INSERT INTO learning (topic) VALUES (?)",
            (topic,)
        )

        connection.commit()

        result.config(
            text="Current: " + topic,
            fg=ACCENT
        )

    save_button = tk.Button(
        learning_window,
        text="Save Topic",
        command=save_topic,
        font=("Arial", 10, "bold"),
        bg=ACCENT,
        fg=BG,
        activebackground=ACCENT,
        relief="flat",
        padx=15,
        pady=7
    )
    save_button.pack(pady=10)


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


# =========================================================
# PROJECTS
# =========================================================

def show_projects():

    projects_window = tk.Toplevel(window)
    projects_window.title("Projects")
    projects_window.geometry("450x400")
    projects_window.configure(bg=BG)

    title = tk.Label(
        projects_window,
        text="MY PROJECTS",
        font=("Arial", 20, "bold"),
        bg=BG,
        fg=ACCENT
    )
    title.pack(pady=25)

    name_label = tk.Label(
        projects_window,
        text="Enter project name:",
        font=("Arial", 14),
        bg=BG,
        fg=TEXT
    )
    name_label.pack(pady=10)

    name_entry = tk.Entry(
        projects_window,
        font=("Arial", 14),
        bg=CARD,
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat"
    )
    name_entry.pack(pady=10)

    status_label = tk.Label(
        projects_window,
        text="Enter project status:",
        font=("Arial", 14),
        bg=BG,
        fg=TEXT
    )
    status_label.pack(pady=10)

    status_entry = tk.Entry(
        projects_window,
        font=("Arial", 14),
        bg=CARD,
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat"
    )
    status_entry.pack(pady=10)

    result = tk.Label(
        projects_window,
        text="",
        font=("Arial", 12),
        bg=BG,
        fg=SECONDARY
    )
    result.pack(pady=10)

    def save_project():

        name = name_entry.get().strip()
        status = status_entry.get().strip()

        if name == "":
            result.config(
                text="Please enter a project name.",
                fg=ACCENT
            )
            return

        cursor.execute(
            "INSERT INTO projects (name, status) VALUES (?, ?)",
            (name, status)
        )

        connection.commit()

        result.config(
            text="Project: " + name + "\nStatus: " + status,
            fg=ACCENT
        )

    save_button = tk.Button(
        projects_window,
        text="Save Project",
        command=save_project,
        font=("Arial", 10, "bold"),
        bg=ACCENT,
        fg=BG,
        activebackground=ACCENT,
        relief="flat",
        padx=15,
        pady=7
    )
    save_button.pack(pady=10)


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


# =========================================================
# CAREER
# =========================================================

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


# =========================================================
# IDEAS
# =========================================================

def show_ideas():

    ideas_window = tk.Toplevel(window)
    ideas_window.title("Ideas Vault")
    ideas_window.geometry("450x400")
    ideas_window.configure(bg=BG)

    title = tk.Label(
        ideas_window,
        text="MY AI IDEAS",
        font=("Arial", 20, "bold"),
        bg=BG,
        fg=ACCENT
    )
    title.pack(pady=25)

    idea_label = tk.Label(
        ideas_window,
        text="Enter your AI idea:",
        font=("Arial", 14),
        bg=BG,
        fg=TEXT
    )
    idea_label.pack(pady=10)

    idea_entry = tk.Entry(
        ideas_window,
        font=("Arial", 14),
        bg=CARD,
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat"
    )
    idea_entry.pack(pady=10)

    result = tk.Label(
        ideas_window,
        text="",
        font=("Arial", 12),
        bg=BG,
        fg=SECONDARY
    )
    result.pack(pady=10)

    def save_idea():

        idea = idea_entry.get().strip()

        if idea == "":
            result.config(
                text="Please enter an idea.",
                fg=ACCENT
            )
            return

        cursor.execute(
            "INSERT INTO ideas (idea) VALUES (?)",
            (idea,)
        )

        connection.commit()

        result.config(
            text="Idea saved: " + idea,
            fg=ACCENT
        )

    save_button = tk.Button(
        ideas_window,
        text="Save Idea",
        command=save_idea,
        font=("Arial", 10, "bold"),
        bg=ACCENT,
        fg=BG,
        activebackground=ACCENT,
        relief="flat",
        padx=15,
        pady=7
    )
    save_button.pack(pady=10)


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


# =========================================================
# DAILY TRACKER
# =========================================================

def show_tracker():

    tracker_window = tk.Toplevel(window)
    tracker_window.title("Daily Tracker")
    tracker_window.geometry("450x450")
    tracker_window.configure(bg=BG)

    title = tk.Label(
        tracker_window,
        text="DAILY TRACKER",
        font=("Arial", 20, "bold"),
        bg=BG,
        fg=ACCENT
    )
    title.pack(pady=25)

    hours_label = tk.Label(
        tracker_window,
        text="Study hours today:",
        font=("Arial", 14),
        bg=BG,
        fg=TEXT
    )
    hours_label.pack(pady=10)

    hours_entry = tk.Entry(
        tracker_window,
        font=("Arial", 14),
        bg=CARD,
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat"
    )
    hours_entry.pack(pady=10)

    result = tk.Label(
        tracker_window,
        text="",
        font=("Arial", 13),
        bg=BG,
        fg=SECONDARY
    )
    result.pack(pady=15)

    today = date.today().isoformat()

    # Show today's saved hours if available
    cursor.execute(
        "SELECT hours FROM tracker WHERE date = ?",
        (today,)
    )

    saved_hours = cursor.fetchone()

    if saved_hours:
        old_hours = saved_hours[0]

        if old_hours >= 3:
            old_message = "Daily target completed! 🔥"
        elif old_hours >= 1.5:
            old_message = "Good progress! 💪"
        else:
            old_message = "Keep going! 🚀"

        result.config(
            text="Today's saved hours: "
            + str(old_hours)
            + "\n"
            + old_message,
            fg=ACCENT
        )

    def save_tracker():

        try:
            hours = float(hours_entry.get())
        except ValueError:
            result.config(
                text="Please enter a valid number.",
                fg=ACCENT
            )
            return

        if hours < 0:
            result.config(
                text="Hours cannot be negative.",
                fg=ACCENT
            )
            return

        if hours >= 3:
            tracker_message = "Daily target completed! 🔥"
        elif hours >= 1.5:
            tracker_message = "Good progress! 💪"
        else:
            tracker_message = "Keep going! 🚀"

        # Save today's hours
        cursor.execute(
            """
            INSERT OR REPLACE INTO tracker (date, hours)
            VALUES (?, ?)
            """,
            (today, hours)
        )

        connection.commit()

        # Update main dashboard progress
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

        result.config(
            text="Study Hours: "
            + str(hours)
            + "\n"
            + tracker_message,
            fg=ACCENT
        )

    save_button = tk.Button(
        tracker_window,
        text="Save Progress",
        command=save_tracker,
        font=("Arial", 10, "bold"),
        bg=ACCENT,
        fg=BG,
        activebackground=ACCENT,
        relief="flat",
        padx=15,
        pady=7
    )
    save_button.pack(pady=10)


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


# =========================================================
# CLOSE DATABASE PROPERLY
# =========================================================

def close_app():

    connection.close()
    window.destroy()


window.protocol("WM_DELETE_WINDOW", close_app)


# =========================================================
# START
# =========================================================

window.mainloop()