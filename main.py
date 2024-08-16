import tkinter as tk
from tkinter import ttk
import subprocess
import importlib.util
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
# Function to dynamically load a module from a file path
def load_module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def launch_image_ascii_app():
    # Load and run ImageASCII_app.py from the apps folder
    ascii_app_path = os.path.join(os.path.dirname(__file__), 'apps', 'ImageASCII_app.py')
    ascii_app = load_module_from_file('ImageASCII_app', ascii_app_path)
    # Start the ASCII Art Generator app
    subprocess.Popen(["python", ascii_app_path])

def launch_image_resize_app():
    # Load and run ImageResize_app.py from the apps folder
    resize_app_path = os.path.join(os.path.dirname(__file__), 'apps', 'ImageResize_app.py')
    resize_app = load_module_from_file('ImageResize_app', resize_app_path)
    # Start the Image Resizer app
    subprocess.Popen(["python", resize_app_path])

# Create the main menu window
root = tk.Tk()
root.title("BulkPix - Menu")
root.geometry("300x200")

# Define the light theme colors
bg_color = "#F0F0F0"
fg_color = "#000000"
button_bg = "#DDDDDD"
button_fg = "#000000"

# Apply light theme
root.configure(bg=bg_color)

# Create and configure the style
style = ttk.Style()
style.configure('TButton', background=button_bg, foreground=button_fg, relief="flat")
style.configure('TLabel', background=bg_color, foreground=fg_color)

# Create and place widgets
ttk.Label(root, text="Select an application:", font=("Arial", 11)).pack(pady=20)

# Create frame to hold the buttons and emojis
button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(padx=10, pady=10)

# Create and place the Bulk Image Resizer button with emoji
resize_button = ttk.Button(button_frame, text="Bulk Image Resizer", command=launch_image_resize_app)
resize_button.grid(row=0, column=1, padx=(0, 10), pady=5)

resize_emoji = tk.Label(button_frame, text="🔄", font=("Arial", 16), bg=bg_color)
resize_emoji.grid(row=0, column=0, padx=(0, 10), pady=5)

# Create and place the ASCII Art Generator button with emoji
ascii_button = ttk.Button(button_frame, text="ASCII Art Generator", command=launch_image_ascii_app)
ascii_button.grid(row=1, column=1, padx=(0, 10), pady=5)

ascii_emoji = tk.Label(button_frame, text="🎨", font=("Arial", 16), bg=bg_color)
ascii_emoji.grid(row=1, column=0, padx=(0, 10), pady=5)

# Start the GUI event loop
root.mainloop()