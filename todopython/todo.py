import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoApp:
    def __init__(self, root):
        self.tasks = []
        
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=20)
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=20)
        
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)
        
        add_btn = tk.Button(btn_frame, text="Add", command=self.add_task)
        add_btn.grid(row=0, column=0)
        
        delete_btn = tk.Button(btn_frame, text="Delete", command=self.delete_task)
        delete_btn.grid(row=0, column=1)
        
        update_btn = tk.Button(btn_frame, text="Update", command=self.update_task)
        update_btn.grid(row=0, column=2)
        
    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_task_index)
            self.tasks.pop(selected_task_index)
        except IndexError:
            pass

    def update_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            new_task = simpledialog.askstring("Update task", "What's the new task?")
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.listbox.delete(selected_task_index)
                self.listbox.insert(selected_task_index, new_task)
        except IndexError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do List App")
    app = ToDoApp(root)
    root.mainloop()
