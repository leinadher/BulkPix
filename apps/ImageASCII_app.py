import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image
from scripts.ImageASCII import resize, desaturate, pixels_to_ASCII
from apps.utils import main_menu, clear_window

# Script that integrates ImageASCII into a Tinkr app, built into a class

class ImageASCIIApp:
    def __init__(self, root):
        self.root = root
        self.art_window = None
        self.current_ascii_art = None
        self.setup_widgets()

    def setup_widgets(self):
        # Define width options
        width_options = [16, 32, 64, 128, 256]

        ttk.Label(self.root, text="Select width in pixels:").pack(padx=10, pady=5)

        self.width_var = tk.IntVar()
        self.width_var.set(width_options[0])  # Default value
        width_menu = ttk.Combobox(self.root, values=width_options, state="readonly", textvariable=self.width_var)
        width_menu.pack(padx=10, pady=5)

        generate_button = ttk.Button(self.root, text="Input image", command=self.generate_ascii_art)
        generate_button.pack(padx=10, pady=10)

        self.message_label = ttk.Label(self.root, text="Select an image and width to generate ASCII art.",
                                       wraplength=350)
        self.message_label.pack(pady=10)

        # Add Back button
        back_button = ttk.Button(self.root, text="Back", command=self.return_to_main_menu)
        back_button.pack(pady=10)

    def return_to_main_menu(self):
        clear_window(self.root)
        main_menu(self.root)

    def generate_ascii_art(self):
        new_width = self.width_var.get()
        print(f"Selected width: {new_width}")  # Debugging output

        if not new_width:
            self.message_label.config(text="Please select a width from the dropdown.", foreground="red")
            return

        file_path = filedialog.askopenfilename(title="Select Image File",
                                               filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            try:
                im = Image.open(file_path)
                resized_image = resize(im, new_width)
                desaturated_image = desaturate(resized_image)
                ascii_data = pixels_to_ASCII(desaturated_image)

                pixel_count = len(ascii_data)
                ascii_art = "\n".join(ascii_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))

                self.close_ascii_preview()
                self.display_ascii_art(ascii_art)
            except Exception as e:
                self.message_label.config(text=f"Error: {e}", foreground="red")

    def display_ascii_art(self, ascii_art):
        self.art_window = tk.Toplevel(self.root)
        self.art_window.title("ASCII Art Preview")
        self.art_window.geometry("600x400")
        self.art_window.configure(bg="#FFFFFF")

        canvas = tk.Canvas(self.art_window, bg="#FFFFFF")
        canvas.pack(side="left", fill="both", expand=True)

        h_scrollbar = tk.Scrollbar(self.art_window, orient="horizontal", command=canvas.xview)
        h_scrollbar.pack(side="bottom", fill="x")
        v_scrollbar = tk.Scrollbar(self.art_window, orient="vertical", command=canvas.yview)
        v_scrollbar.pack(side="right", fill="y")
        canvas.config(xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)

        frame = tk.Frame(canvas, bg="#FFFFFF")
        canvas.create_window((0, 0), window=frame, anchor="nw")

        font_size = 10
        font = ("Courier New", font_size)
        spacing = font_size

        x, y = 10, 10
        for line in ascii_art.splitlines():
            for char in line:
                canvas.create_text(x, y, text=char, font=font, fill="#000000", anchor="nw")
                x += spacing
            x = 10
            y += spacing

        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        save_button = ttk.Button(self.art_window, text="Save ASCII Art as .txt", command=lambda: self.save_ascii_art(ascii_art))
        save_button.pack(pady=10, side="bottom")

        self.current_ascii_art = ascii_art

    def close_ascii_preview(self):
        if self.art_window and self.art_window.winfo_exists():
            self.art_window.destroy()
        self.art_window = None

    def save_ascii_art(self, ascii_art):
        output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if output_file:
            try:
                with open(output_file, "w") as f:
                    f.write(ascii_art)
                self.message_label.config(text="ASCII art saved successfully!", foreground="green")
            except Exception as e:
                self.message_label.config(text=f"Error saving file: {e}", foreground="red")
        else:
            self.message_label.config(text="Save operation cancelled.", foreground="black")
