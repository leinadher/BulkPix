import tkinter as tk
from tkinter import ttk

def clear_window(root):
    """Function to clear all widgets from the root window."""
    for widget in root.winfo_children():
        widget.destroy()

def main_menu(root):
    """Function to display the main menu."""
    ttk.Label(root, text="Select an application:", font=("Arial", 11)).pack(pady=20)

    button_frame = tk.Frame(root, bg="#F0F0F0")
    button_frame.pack(padx=10, pady=10)

    resize_button = ttk.Button(button_frame, text="Bulk Image Resizer", command=lambda: launch_image_resize_app(root))
    resize_button.grid(row=0, column=1, padx=(0, 10), pady=5)

    resize_emoji = tk.Label(button_frame, text="🔄", font=("Arial", 16), bg="#F0F0F0")
    resize_emoji.grid(row=0, column=0, padx=(0, 10), pady=5)

    ascii_button = ttk.Button(button_frame, text="ASCII Art Generator", command=lambda: launch_image_ascii_app(root))
    ascii_button.grid(row=1, column=1, padx=(0, 10), pady=5)

    ascii_emoji = tk.Label(button_frame, text="🎨", font=("Arial", 16), bg="#F0F0F0")
    ascii_emoji.grid(row=1, column=0, padx=(0, 10), pady=5)

def launch_image_resize_app(root):
    from apps.ImageResize_app import ImageResizeApp
    clear_window(root)
    ImageResizeApp(root)

def launch_image_ascii_app(root):
    from apps.ImageASCII_app import ImageASCIIApp
    clear_window(root)
    ImageASCIIApp(root)
