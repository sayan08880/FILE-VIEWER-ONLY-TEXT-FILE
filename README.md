# Python File Manager (Tkinter GUI)

A simple **GUI-based File Manager built with Python and Tkinter**.
This application allows users to **navigate directories, search files, and open supported files directly from a graphical interface**.

The program runs in **full-screen mode** and provides a **minimal black-themed interface** designed for simple file navigation.

---

# Features

* Full-screen GUI interface
* View files and folders in the current directory
* Navigate folders using simple commands
* Open supported files directly
* Search files and folders
* Exit to parent directory
* Keyboard support (Enter key)
* Styled buttons with hover effects
* Dark theme interface

---

# Interface Overview

The application contains:

* **Directory Viewer**

  * Displays files and folders with index numbers

* **Input Box**

  * Enter commands to navigate or search

* **Buttons**

  * Enter → Open file or enter folder
  * Search → Search for files
  * Exit File → Go to parent folder
  * Exit App → Close the application

---

# Navigation Command

To open a file or enter a folder:

```
v/<number>
```

Example:

```
v/3
```

This will open or enter the **3rd item in the list**.

---

# File Opening Support

Supported file types:

| File Type    | Application     |
| ------------ | --------------- |
| .txt         | Notepad         |
| .log         | Notepad         |
| .ini         | Notepad         |
| .doc / .docx | Microsoft Word  |
| .xls / .xlsx | Microsoft Excel |

Unsupported file types will show an error message.

---

# Search Function

You can search files or folders inside the current directory.

Steps:

1. Type a keyword in the input box
2. Click **Search**
3. Matching files and folders will appear in the display area

---

# Requirements

* Python **3.x**
* Tkinter (usually included with Python)

To check Python version:

```
python --version
```

---

# How to Run

1. Download or clone the repository

```
git clone https://github.com/yourusername/python-file-manager.git
```

2. Go to the project folder

```
cd python-file-manager
```

3. Run the program

```
python file_manager.py
```

---

# Project Structure

```
file_manager.py
README.md
```

---

# Technologies Used

* Python
* Tkinter GUI
* OS module
* Subprocess module

---

# Learning Purpose

This project helps beginners understand:

* Python GUI programming
* File system navigation
* Event handling
* Tkinter widgets
* Working with subprocess and OS modules

---

# Author

**Sayan**

BCA Student
Python GUI Learning Project

---

# License

This project is free to use for **educational purposes**.
