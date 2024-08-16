import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image
import os
from scripts.ImageASCII import resize, desaturate, pixels_to_ASCII

def generate_ascii_art():
    new_width = width_var.get()
    if not new_width:
        message_label.config(text="Please select a width from the dropdown.", foreground="red")
        return

    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        try:
            im = Image.open(file_path)
            resized_image = resize(im, new_width)
            desaturated_image = desaturate(resized_image)
            ascii_data = pixels_to_ASCII(desaturated_image)

            pixel_count = len(ascii_data)
            ascii_art = "\n".join(ascii_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

            # Close the existing ASCII art preview window if it exists
            close_ascii_preview()

            # Open a new window to display the ASCII art
            display_ascii_art(ascii_art)
        except Exception as e:
            message_label.config(text=f"Error: {e}", foreground="red")

def display_ascii_art(ascii_art):
    global art_window
    # Create a new window to display the ASCII art
    art_window = tk.Toplevel(root)
    art_window.title("ASCII Art Preview")

    # Set a smaller size for the preview window
    art_window.geometry("600x400")
    art_window.configure(bg="#FFFFFF")

    # Create a Canvas widget with scrollbars
    canvas = tk.Canvas(art_window, bg="#FFFFFF")
    canvas.pack(side="left", fill="both", expand=True)

    h_scrollbar = tk.Scrollbar(art_window, orient="horizontal", command=canvas.xview)
    h_scrollbar.pack(side="bottom", fill="x")
    v_scrollbar = tk.Scrollbar(art_window, orient="vertical", command=canvas.yview)
    v_scrollbar.pack(side="right", fill="y")
    canvas.config(xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)

    # Create a frame to hold the Canvas
    frame = tk.Frame(canvas, bg="#FFFFFF")
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Define font and spacing
    font_size = 10  # Adjust font size for better fit
    font = ("Courier New", font_size)
    spacing = font_size  # Adjust spacing as needed

    # Add ASCII art to the canvas
    x, y = 10, 10  # Starting position
    for line in ascii_art.splitlines():
        for char in line:
            canvas.create_text(x, y, text=char, font=font, fill="#000000", anchor="nw")
            x += spacing
        x = 10
        y += spacing

    # Update the canvas scroll region
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Add Save button to the art_window
    save_button = ttk.Button(art_window, text="Save ASCII Art", command=lambda: save_ascii_art(ascii_art))
    save_button.pack(pady=10, side="bottom")

    # Store ASCII art in a global variable
    global current_ascii_art
    current_ascii_art = ascii_art

def close_ascii_preview():
    global art_window
    if art_window and art_window.winfo_exists():
        art_window.destroy()
    art_window = None

def save_ascii_art(ascii_art):
    output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if output_file:
        try:
            with open(output_file, "w") as f:
                f.write(ascii_art)
            message_label.config(text="ASCII art saved successfully!", foreground="green")
        except Exception as e:
            message_label.config(text=f"Error saving file: {e}", foreground="red")
    else:
        message_label.config(text="Save operation cancelled.", foreground="black")

# Create the main window
root = tk.Tk()
root.title("BulkPix - ASCII Art Generator")
root.geometry("400x350")

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

# Define the width options for the dropdown menu
width_options = [16, 32, 64, 128, 256]

# Create and place widgets
ttk.Label(root, text="Select width in pixels:").pack(padx=10, pady=5)

width_var = tk.IntVar(value=width_options[0])  # Default to the first option
width_menu = ttk.Combobox(root, textvariable=width_var, values=width_options, state="readonly")
width_menu.pack(padx=10, pady=5)

generate_button = ttk.Button(root, text="Input image", command=generate_ascii_art)
generate_button.pack(padx=10, pady=10)

# Label for displaying messages and instructions
message_label = ttk.Label(root, text="Select an image and width to generate ASCII art.", wraplength=350)
message_label.pack(pady=10)

# Initialize variables
current_ascii_art = None
art_window = None

# Start the GUI event loop
root.mainloop()
