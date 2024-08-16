import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image
import os
from scripts.ImageASCII import resize, desaturate, pixels_to_ASCII

def generate_ascii_art():
    new_width = width_entry.get()
    if not new_width.isdigit():
        message_label.config(text="Please enter a valid integer for width.", foreground="red")
        return

    new_width = int(new_width)
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        try:
            im = Image.open(file_path)
            resized_image = resize(im, new_width)
            desaturated_image = desaturate(resized_image)
            ascii_data = pixels_to_ASCII(desaturated_image)

            pixel_count = len(ascii_data)
            ascii_art = "\n".join(ascii_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

            output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if output_file:
                with open(output_file, "w") as f:
                    f.write(ascii_art)
                message_label.config(text="ASCII art saved successfully!", foreground="green")
            else:
                message_label.config(text="Save operation cancelled.", foreground="blue")
        except Exception as e:
            message_label.config(text=f"Error: {e}", foreground="red")

# Create the main window
root = tk.Tk()
root.title("BulkPix - ASCII Art Generator")
root.geometry("400x250")

# Light theme colors
bg_color = "#F0F0F0"
fg_color = "#000000"
button_bg = "#DDDDDD"
button_fg = "#000000"
message_fg = "#000000"

# Apply light theme
root.configure(bg=bg_color)

# Create and configure the style
style = ttk.Style()
style.configure('TButton', background=button_bg, foreground=button_fg, relief="flat")
style.configure('TLabel', background=bg_color, foreground=fg_color)

# Create and place widgets
ttk.Label(root, text="New width in pixels:").pack(padx=10, pady=5)
width_entry = tk.Entry(root, background="#FFFFFF", foreground=fg_color)
width_entry.pack(padx=10, pady=5)

generate_button = ttk.Button(root, text="Image input", command=generate_ascii_art)
generate_button.pack(padx=10, pady=10)

# Label for displaying messages and instructions
message_label = ttk.Label(root, text="Select an image and specify width to generate ASCII art.", wraplength=350)
message_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
