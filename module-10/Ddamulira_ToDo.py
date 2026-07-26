# Name: Peter Ddamulira
# Assignment: Module 10 - GUI ToDo
# Description:
# This program creates a Tkinter To-Do List application.
# Users can add tasks, delete tasks using the right mouse button,
# and exit the program through the File menu.

import tkinter as tk
from tkinter import simpledialog


class ToDoApp:
    """A simple Tkinter To-Do List application."""

    def __init__(self, root):
        self.root = root

        # Requirement: Change window title to last name-ToDo
        self.root.title("Ddamulira-ToDo")
        self.root.geometry("450x500")

        # Create the File menu
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)

        # Requirement: File -> Exit
        file_menu.add_command(label="Exit", command=self.root.destroy)

        menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu_bar)

        # Instructions
        self.instructions = tk.Label(
            self.root,
            text="Add a task below — Right-click a task to delete it.",
            font=("Arial", 11, "bold"),
            pady=10
        )
        self.instructions.pack(fill="x")

        # Entry box
        self.task_entry = tk.Entry(
            self.root,
            font=("Arial", 12)
        )
        self.task_entry.pack(
            fill="x",
            padx=15,
            pady=5
        )

        # Add Task button
        self.add_button = tk.Button(
            self.root,
            text="Add Task",
            command=self.add_task,
            font=("Arial", 11)
        )
        self.add_button.pack(pady=5)

        # Scrollable task area
        self.canvas = tk.Canvas(self.root)

        self.scrollbar = tk.Scrollbar(
            self.root,
            orient="vertical",
            command=self.canvas.yview
        )

        self.task_frame = tk.Frame(self.canvas)

        self.task_frame.bind(
            "<Configure>",
            lambda event: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window(
            (0, 0),
            window=self.task_frame,
            anchor="nw",
            width=415
        )

        self.canvas.configure(
            yscrollcommand=self.scrollbar.set
        )

        self.canvas.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(15, 0),
            pady=10
        )

        self.scrollbar.pack(
            side="right",
            fill="y",
            pady=10,
            padx=(0, 15)
        )

        # Two complementary task colors
        self.colors = ["#6A0DAD", "#FFD700"]
        self.task_count = 0

        # Pressing Enter also adds a task
        self.task_entry.bind("<Return>", self.add_task)

    def add_task(self, event=None):
        """Add a new task to the To-Do List."""

        task_text = self.task_entry.get().strip()

        if task_text == "":
            return

        color = self.colors[self.task_count % 2]

        # Use dark text on yellow and white text on purple
        text_color = "black" if color == "#FFD700" else "white"

        task_label = tk.Label(
            self.task_frame,
            text=task_text,
            bg=color,
            fg=text_color,
            font=("Arial", 11),
            pady=10
        )

        task_label.pack(
            fill="x",
            pady=2
        )

        # Requirement: RIGHT mouse button deletes a task
        task_label.bind("<Button-3>", self.delete_task)

        self.task_count += 1

        # Clear entry after task is added
        self.task_entry.delete(0, tk.END)

    def delete_task(self, event):
        """Delete a task when the user right-clicks it."""

        event.widget.destroy()


def main():
    """Start the To-Do List application."""

    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()