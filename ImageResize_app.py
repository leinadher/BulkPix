import tkinter as tk
from tkinter import filedialog, ttk
from scripts.ImageResize import resize_image
import os
import platform

def resize_all_images_in_folder(folder_path, new_width, output_folder):
    try:
        files = os.listdir(folder_path)
        image_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

        if not image_files:
            message_label.config(text="No image files found in the selected folder.", foreground="blue")
            return

        num_images = len(image_files)
        for file in image_files:
            file_path = os.path.join(folder_path, file)
            output_path = resize_image(file_path, new_width, output_folder)
            print(f"Processed {file_path}, saved to {output_path}")

        message_label.config(text=f"{num_images} images resized and saved.", foreground="green")
        open_output_button.config(state=tk.NORMAL)  # Enable the button after resizing
    except Exception as e:
        message_label.config(text=f"Error: {e}", foreground="red")

def open_output_directory():
    try:
        if platform.system() == "Windows":
            os.startfile(output_folder)  # Windows
        elif platform.system() == "Darwin":
            os.system(f'open "{output_folder}"')  # macOS
        elif platform.system() == "Linux":
            os.system(f'xdg-open "{output_folder}"')  # Linux
    except Exception as e:
        message_label.config(text=f"Error opening folder: {e}", foreground="red")

def on_resize_button_click():
    global output_folder  # Make output_folder global to access in open_output_directory
    new_width = width_entry.get()
    if not new_width.isdigit():
        message_label.config(text="You must first enter a valid width value.", foreground="red")
        return

    new_width = int(new_width)
    folder_path = filedialog.askdirectory(title="Select Folder with Images")
    if folder_path:
        output_folder = filedialog.askdirectory(title="Select Output Folder")
        if output_folder:
            resize_all_images_in_folder(folder_path, new_width, output_folder)

# Create the main window
root = tk.Tk()
root.title("BulkPix - Image Resize")
# Set the window size (width x height)
root.geometry("400x250")  # Adjust the size to accommodate the new button

# Light theme colors
bg_color = "#F0F0F0"  # Light gray background
fg_color = "#000000"  # Black text
button_bg = "#DDDDDD"  # Light gray button background
button_fg = "#000000"  # Black button text
message_fg = "#000000"  # Black text for messages

# Apply light theme
root.configure(bg=bg_color)

# Create and configure the style
style = ttk.Style()
style.configure('TButton', background=button_bg, foreground=button_fg, relief="flat")
style.configure('TLabel', background=bg_color, foreground=fg_color)

# Create and place widgets with light theme
ttk.Label(root, text="New width in pixels:").pack(padx=10, pady=5)
width_entry = tk.Entry(root, background="#FFFFFF", foreground=fg_color)
width_entry.pack(padx=10, pady=5)

resize_button = ttk.Button(root, text="Input folder", command=on_resize_button_click)
resize_button.pack(padx=10, pady=10)

open_output_button = ttk.Button(root, text="Output folder", command=open_output_directory, state=tk.DISABLED)
open_output_button.pack(padx=10, pady=10)

# Label for displaying messages and instructions
message_label = ttk.Label(root,
                         text="Enter new width in pixels and click 'Input folder' to select images.",
                         wraplength=350)
message_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
