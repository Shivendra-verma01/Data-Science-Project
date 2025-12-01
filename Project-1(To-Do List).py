#To-Do List
import tkinter as tk
from tkinter import messagebox

def add_task():

    task = task_entry.get()

    if task.strip() == "": 
        messagebox.showwarning("Warning", "Please enter a task.")
        
    else:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)

    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create main window
root = tk.Tk()
root.title("To-Do List")

# Entry widget to enter tasks
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Add Task button
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Delete Task button
delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

# Run the GUI event loop
root.mainloop()
