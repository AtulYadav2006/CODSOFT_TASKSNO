import tkinter as tk
from tkinter import messagebox


# ---------------- CREATE TASK ----------------
def add_new_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task.")
        return

    task_list.insert(tk.END, f"Pending | {task}")
    task_entry.delete(0, tk.END)

    update_count()


# ---------------- UPDATE TASK ----------------
def update_task():
    selected = task_list.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Please select a task.")
        return

    new_task = task_entry.get().strip()

    if new_task == "":
        messagebox.showwarning("Warning", "Enter the updated task.")
        return

    index = selected[0]

    old_task = task_list.get(index)

    # Keep the current status
    status = old_task.split(" | ")[0]

    task_list.delete(index)
    task_list.insert(index, f"{status} | {new_task}")

    task_entry.delete(0, tk.END)

    update_count()


# ---------------- MARK COMPLETED ----------------
def mark_completed():
    selected = task_list.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Please select a task.")
        return

    index = selected[0]
    task = task_list.get(index)

    task_name = task.split(" | ", 1)[1]

    task_list.delete(index)
    task_list.insert(index, f"Completed | {task_name}")

    update_count()


# ---------------- DELETE TASK ----------------
def delete_task():
    selected = task_list.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Please select a task.")
        return

    task_list.delete(selected[0])

    update_count()


# ---------------- CLEAR ALL ----------------
def clear_all():
    if task_list.size() == 0:
        return

    confirm = messagebox.askyesno(
        "Confirm",
        "Do you want to delete all tasks?"
    )

    if confirm:
        task_list.delete(0, tk.END)
        update_count()


# ---------------- TRACK TASKS ----------------
def update_count():
    total = task_list.size()
    completed = 0
    pending = 0

    for i in range(total):
        task = task_list.get(i)

        if task.startswith("Completed"):
            completed += 1
        else:
            pending += 1

    total_label.config(text=f"Total: {total}")
    pending_label.config(text=f"Pending: {pending}")
    completed_label.config(text=f"Completed: {completed}")


# ---------------- MAIN WINDOW ----------------
root = tk.Tk()

root.title("To-Do List Manager")
root.geometry("650x600")
root.resizable(False, False)


# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="To-Do List Manager",
    font=("Arial", 26, "bold")
)

title.pack(pady=20)


# ---------------- INPUT ----------------
task_entry = tk.Entry(
    root,
    font=("Arial", 15),
    width=40
)

task_entry.pack(pady=10)


# ---------------- BUTTON FRAME ----------------
button_frame = tk.Frame(root)
button_frame.pack(pady=10)


add_button = tk.Button(
    button_frame,
    text="Create Task",
    width=14,
    command=add_new_task
)

add_button.grid(row=0, column=0, padx=5)


update_button = tk.Button(
    button_frame,
    text="Update Task",
    width=14,
    command=update_task
)

update_button.grid(row=0, column=1, padx=5)


complete_button = tk.Button(
    button_frame,
    text="Mark Completed",
    width=14,
    command=mark_completed
)

complete_button.grid(row=0, column=2, padx=5)


# ---------------- TASK LIST ----------------
task_list = tk.Listbox(
    root,
    font=("Arial", 14),
    width=55,
    height=15
)

task_list.pack(pady=20)


# ---------------- DELETE & CLEAR ----------------
delete_button = tk.Button(
    root,
    text="Delete Selected",
    width=18,
    command=delete_task
)

delete_button.pack(pady=5)


clear_button = tk.Button(
    root,
    text="Clear All",
    width=18,
    command=clear_all
)

clear_button.pack(pady=5)


# ---------------- TRACKING ----------------
tracking_frame = tk.Frame(root)
tracking_frame.pack(pady=15)


total_label = tk.Label(
    tracking_frame,
    text="Total: 0",
    font=("Arial", 12, "bold")
)

total_label.grid(row=0, column=0, padx=20)


pending_label = tk.Label(
    tracking_frame,
    text="Pending: 0",
    font=("Arial", 12, "bold")
)

pending_label.grid(row=0, column=1, padx=20)


completed_label = tk.Label(
    tracking_frame,
    text="Completed: 0",
    font=("Arial", 12, "bold")
)

completed_label.grid(row=0, column=2, padx=20)


# ---------------- RUN APP ----------------
root.mainloop()