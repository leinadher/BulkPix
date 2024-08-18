import tkinter as tk
from tkinter import ttk
import webbrowser

# Main app script, launching menu interface and navigation utilities

# Clears which ever app/window is loaded
def clear_window(root):
    """Function to clear all widgets from the root window."""
    for widget in root.winfo_children():
        widget.destroy()

# Executes the main menu
def main_menu(root):
    """Function to display the main menu."""
    ttk.Label(root, text="Select an application:", font=("Arial", 11)).pack(pady=20)

    # Frame that contains the buttons / widgets
    button_frame = tk.Frame(root, bg="#F0F0F0")
    button_frame.pack(padx=10, pady=10)

    # Bulk Image Resizer button
    resize_button = ttk.Button(button_frame, text="Bulk Image Resizer", command=lambda: launch_image_resize_app(root))
    resize_button.grid(row=0, column=1, sticky='w', padx=(0, 10), pady=5)

    resize_emoji = tk.Label(button_frame, text="🔄", font=("Arial", 18), bg="#F0F0F0")
    resize_emoji.grid(row=0, column=0, sticky='w', padx=(0, 10), pady=5)

    # ASCII Art Generator button
    ascii_button = ttk.Button(button_frame, text="ASCII Art Generator", command=lambda: launch_image_ascii_app(root))
    ascii_button.grid(row=1, column=1, sticky='w', padx=(0, 10), pady=5)

    ascii_emoji = tk.Label(button_frame, text="🎨", font=("Arial", 18), bg="#F0F0F0")
    ascii_emoji.grid(row=1, column=0, sticky='w', padx=(0, 10), pady=5)

    # GitHub link
    def open_github():
        webbrowser.open("https://github.com/leinadher/BulkPix")

    github_button = ttk.Button(button_frame, text="GitHub Project", command=open_github)
    github_button.grid(row=2, column=1, sticky='w', padx=(0, 10), pady=5)

    github_emoji = tk.Label(button_frame, text="🛠️", font=("Arial", 18), bg="#F0F0F0")
    github_emoji.grid(row=2, column=0, sticky='w', padx=(0, 10), pady=5)


# Sub-app launch functions
def launch_image_resize_app(root):
    from apps.ImageResize_app import ImageResizeApp
    clear_window(root)
    ImageResizeApp(root)

def launch_image_ascii_app(root):
    from apps.ImageASCII_app import ImageASCIIApp
    clear_window(root)
    ImageASCIIApp(root)
