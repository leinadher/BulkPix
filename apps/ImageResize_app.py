import tkinter as tk
from tkinter import filedialog, ttk
from scripts.ImageResize import resize_image
import os
import platform
from apps.utils import main_menu, clear_window

# Script that integrates ImageResize into a Tinkr app, built into a class

class ImageResizeApp:
    def __init__(self, root):
        self.root = root
        self.output_folder = None
        self.setup_widgets()

    def setup_widgets(self):
        ttk.Label(self.root, text="New width in pixels:").pack(padx=10, pady=5)

        # Text entry box
        self.width_entry = tk.Entry(self.root, background="#FFFFFF", foreground="#000000")
        self.width_entry.pack(padx=10, pady=5)

        # Input folder button
        resize_button = ttk.Button(self.root, text="Input folder", command=self.on_resize_button_click)
        resize_button.pack(padx=10, pady=10)

        # Output folder button
        self.open_output_button = ttk.Button(self.root, text="Open output folder", command=self.open_output_directory,
                                             state=tk.DISABLED)
        self.open_output_button.pack(padx=10, pady=10)

        # Info label
        self.message_label = ttk.Label(self.root,
                                       text="Enter new width in pixels and click 'Input folder' to select images.",
                                       wraplength=350)
        self.message_label.pack(pady=10)

        # Back button
        back_button = ttk.Button(self.root, text="Back", command=self.return_to_main_menu)
        back_button.pack(pady=10)

    def return_to_main_menu(self):
        clear_window(self.root)
        main_menu(self.root)

    def resize_all_images_in_folder(self, folder_path, new_width, output_folder):
        try:
            files = os.listdir(folder_path)
            image_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

            if not image_files:
                self.message_label.config(text="No image files found in the selected folder.", foreground="blue")
                return

            num_images = len(image_files)
            for file in image_files:
                file_path = os.path.join(folder_path, file)
                output_path = resize_image(file_path, new_width, output_folder)
                print(f"Processed {file_path}, saved to {output_path}")

            self.message_label.config(text=f"{num_images} images resized and saved.", foreground="green")
            self.open_output_button.config(state=tk.NORMAL)  # Enable the button after resizing
        except Exception as e:
            self.message_label.config(text=f"Error: {e}", foreground="red")

    def open_output_directory(self):
        if self.output_folder:
            try:
                if platform.system() == "Windows":
                    os.startfile(self.output_folder)  # Windows
                elif platform.system() == "Darwin":
                    os.system(f'open "{self.output_folder}"')  # macOS
                elif platform.system() == "Linux":
                    os.system(f'xdg-open "{self.output_folder}"')  # Linux
            except Exception as e:
                self.message_label.config(text=f"Error opening folder: {e}", foreground="red")

    def on_resize_button_click(self):
        new_width = self.width_entry.get()
        if not new_width.isdigit():
            self.message_label.config(text="You must first enter a valid width value.", foreground="red")
            return

        new_width = int(new_width)
        folder_path = filedialog.askdirectory(title="Select Folder with Images")
        if folder_path:
            self.output_folder = filedialog.askdirectory(title="Select Output Folder")
            if self.output_folder:
                self.resize_all_images_in_folder(folder_path, new_width, self.output_folder)
