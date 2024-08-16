import tkinter as tk
from tkinter import ttk
from apps.ImageResize_app import ImageResizeApp
from apps.ImageASCII_app import ImageASCIIApp

def launch_image_ascii_app():
    clear_window()
    ImageASCIIApp(root)

def launch_image_resize_app():
    clear_window()
    ImageResizeApp(root)

def clear_window():
    # Remove all widgets from the current window
    for widget in root.winfo_children():
        widget.destroy()

# Create the main menu window
root = tk.Tk()
root.title("BulkPix")
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
ttk.Label(root, text="Choose an application:", font=("Arial", 11)).pack(pady=20)

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
