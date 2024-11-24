import tkinter as tk
import os


class ToDoList:
    def __init__(self):
        # Main Window for my todo list
        self.calc_main_window = tk.Tk()
        self.calc_main_window.geometry("300x400")
        self.calc_main_window.title("ToDo List")

        # Frames
        self.top_frame = tk.Frame(self.calc_main_window)
        self.bottom_frame = tk.Frame(self.calc_main_window)
        self.message_frame = tk.Frame(self.calc_main_window)

        # Task Entry
        self.task_entry = tk.Entry(self.top_frame, width=30)
        self.task_entry.pack(pady=10, side="left")

        # Task Submit Button
        self.add_task_button = tk.Button(self.top_frame, text="Add", command=self.add_task)
        self.add_task_button.pack(side="left")

        # Ensure the file exists
        if not os.path.exists("todo_list.txt"):
            open("todo_list.txt", "w").close()

        # Read and display the tasks
        self.display_tasks()

        # My message
        self.message = tk.Label(self.calc_main_window, text="Made with ❤ by Esmat Hadi.")
        self.message.pack(side="bottom", pady=10)

        # Pack Frames
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.message_frame.pack()

        tk.mainloop()

    def display_tasks(self):
        for widget in self.bottom_frame.winfo_children():
            widget.destroy()

        # Read tasks from the file
        with open("todo_list.txt", "r") as read_file:
            task_items = read_file.readlines()

        # Create a new label and button for each task
        for task in task_items:
            task = task.strip()
            if task:
                new_frame = tk.Frame(self.bottom_frame)
                tk.Label(new_frame, text=task).pack(side="left")
                tk.Button(new_frame, text="Done", command=lambda t=task: self.delete_task(t)).pack(side="left")
                new_frame.pack()

    def add_task(self):
        new_task = self.task_entry.get().strip()
        if new_task:
            with open("todo_list.txt", "a") as task_file:
                task_file.write(new_task + "\n")
            self.task_entry.delete(0, tk.END)  # Clear the entry field
            self.display_tasks()  # Refresh the task list after a task is added

    def delete_task(self, task):
        with open("todo_list.txt", "r") as task_file:
            tasks = task_file.readlines()
        with open("todo_list.txt", "w") as task_file:
            for line in tasks:
                if line.strip() != task:
                    task_file.write(line)
        self.display_tasks()  # Refresh the task list after a task is deleted


if __name__ == "__main__":
    ToDoList()
