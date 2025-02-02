import os
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")
        self.root.attributes('-fullscreen', True)  # Open in full-screen mode
        self.root.configure(bg="black")
        self.current_directory = os.getcwd()

        # Custom styling
        self.button_style = {
            "background": "#4CAF50",  # Green color
            "foreground": "white",    # Text color
            "font": ("Arial", 10, "bold"),
            "borderwidth": 0,
            "relief": "flat",
            "activebackground": "#45a049",  # Darker green when clicked
            "activeforeground": "white",
            "width": 15,  # Medium button size
            "padx": 10,
            "pady": 5,
        }

        self.create_widgets()
        self.update_listbox()

        # Bind Enter key to enter_folder_or_open_file
        self.root.bind('<Return>', self.enter_folder_or_open_file_key)

    def create_widgets(self):
        # Text area to display directory contents
        self.text_area = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, width=100, height=25, bg="black", fg="white", insertbackground="white"
        )
        self.text_area.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Make the window resizable by adding weights
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Input box, larger and centered
        screen_width = self.root.winfo_screenwidth()
        self.entry_field = tk.Entry(self.root, width=int(screen_width * 0.5 // 10), bg="white", fg="black")
        self.entry_field.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Buttons for actions
        self.enter_button = self.create_rounded_button("Enter", self.enter_folder_or_open_file)
        self.enter_button.grid(row=2, column=0, sticky="w", padx=(10, 5), pady=5)

        self.search_button = self.create_rounded_button("Search", self.search_folder)
        self.search_button.grid(row=3, column=0, sticky="w", padx=(10, 5), pady=5)

        self.exit_file_button = self.create_rounded_button("Exit File", self.exit_folder)
        self.exit_file_button.grid(row=2, column=1, sticky="e", padx=(5, 10), pady=5)

        self.exit_app_button = self.create_rounded_button("Exit App", self.root.quit)
        self.exit_app_button.grid(row=3, column=1, sticky="e", padx=(5, 10), pady=5)

    def create_rounded_button(self, text, command):
        """Create a button with rounded corners and hover effects."""
        button = tk.Button(
            self.root,
            text=text,
            command=command,
            **self.button_style,
        )
        button.config(
            highlightbackground=self.button_style["background"],
            highlightcolor=self.button_style["background"],
            border=2,  # Add rounded corners
            relief="raised",
        )

        # Add hover effects
        button.bind("<Enter>", lambda e: button.config(background="#45a049"))  # Darker green on hover
        button.bind("<Leave>", lambda e: button.config(background="#4CAF50"))  # Revert to original color

        return button

    def update_listbox(self):
        """Update the text area with the current directory contents."""
        self.text_area.delete(1.0, tk.END)
        items = os.listdir(self.current_directory)
        for index, item in enumerate(items, start=1):
            self.text_area.insert(tk.END, f"{index}. {item}\n")

    def enter_folder_or_open_file(self):
        """Enter a folder or open a file based on user input."""
        user_input = self.entry_field.get().strip()
        self.process_input(user_input)

    def enter_folder_or_open_file_key(self, event):
        """Handle keyboard Enter key press to enter a file or directory."""
        user_input = self.entry_field.get().strip()
        self.process_input(user_input)

    def process_input(self, user_input):
        if user_input.startswith("v/"):
            try:
                index = int(user_input.split("/")[1]) - 1
                items = os.listdir(self.current_directory)
                if 0 <= index < len(items):
                    selected_item = items[index]
                    new_path = os.path.join(self.current_directory, selected_item)
                    if os.path.isdir(new_path):
                        self.current_directory = new_path
                        self.update_listbox()
                    elif os.path.isfile(new_path):
                        self.open_file(new_path)
                    else:
                        messagebox.showerror("Error", "Invalid item.")
                else:
                    messagebox.showerror("Error", "Invalid index.")
            except (ValueError, IndexError):
                messagebox.showerror("Error", "Invalid input format. Use v/<number>.")
        else:
            messagebox.showerror("Error", "Invalid input. Use v/<number> to enter a folder or open a file.")

    def exit_folder(self):
        """Exit to the parent folder."""
        parent_directory = os.path.dirname(self.current_directory)
        if parent_directory != self.current_directory:
            self.current_directory = parent_directory
            self.update_listbox()
        else:
            messagebox.showerror("Error", "Already at the root directory.")

    def search_folder(self):
        """Search for files or folders in the current directory."""
        search_term = self.entry_field.get().strip()
        if search_term:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, f"Search results for '{search_term}':\n")
            for root, dirs, files in os.walk(self.current_directory):
                for name in files + dirs:
                    if search_term.lower() in name.lower():
                        self.text_area.insert(tk.END, f"{os.path.join(root, name)}\n")
        else:
            messagebox.showerror("Error", "Please enter a search term.")

    def open_file(self, file_path):
        """Open a file in Notepad or MS Office based on file type."""
        try:
            if file_path.endswith((".txt", ".log", ".ini")):
                subprocess.run(["notepad.exe", file_path], check=True)
            elif file_path.endswith((".doc", ".docx")):
                subprocess.run(["start", "winword", file_path], shell=True, check=True)
            elif file_path.endswith((".xls", ".xlsx")):
                subprocess.run(["start", "excel", file_path], shell=True, check=True)
            else:
                messagebox.showerror("Error", "Unsupported file type.")
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Could not open the file.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()