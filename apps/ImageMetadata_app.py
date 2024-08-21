import tkinter as tk
from tkinter import filedialog, ttk
from scripts.ImageMetadata import extract_metadata, extract_specific_exif, metadata_to_dataframe
import os
import platform
from apps.utils import main_menu, clear_window

# Script that integrates ImageMetadata into a Tinkr app, built into a class

class ImageMetadataApp:
    def __init__(self, root):
        self.root = root
        self.metadata_output_folder = None
        self.setup_widgets()

    def setup_widgets(self):
        # Input folder button
        self.select_folder_button = ttk.Button(self.root, text="Input folder", command=self.on_select_folder_button_click)
        self.select_folder_button.pack(padx=10, pady=10)

        # Output folder button
        self.select_output_button = ttk.Button(self.root, text="Save as CSV", command=self.on_select_output_button_click)
        self.select_output_button.pack(padx=10, pady=10)

        # Info label
        self.message_label = ttk.Label(self.root,
                                       text="Select input folder with images and save CSV with metadata.",
                                       wraplength=350)
        self.message_label.pack(pady=10)

        # Extract metadata button
        self.extract_metadata_button = ttk.Button(self.root, text="Extract Metadata", command=self.on_extract_metadata_button_click, state=tk.DISABLED)
        self.extract_metadata_button.pack(padx=10, pady=10)

        # Open output directory button
        self.open_output_directory_button = ttk.Button(self.root, text="Open output folder", command=self.open_metadata_output_directory, state=tk.DISABLED)
        self.open_output_directory_button.pack(padx=10, pady=10)

        # Back button
        back_button = ttk.Button(self.root, text="Back", command=self.return_to_main_menu)
        back_button.pack(pady=10)

    def return_to_main_menu(self):
        clear_window(self.root)
        main_menu(self.root)

    def on_select_folder_button_click(self):
        self.folder_path = filedialog.askdirectory(title="Select Folder with Images")
        if self.folder_path:
            self.check_ready_to_extract()

    def on_select_output_button_click(self):
        self.metadata_output_folder = filedialog.askdirectory(title="Select Metadata Output Folder")
        if self.metadata_output_folder:
            self.check_ready_to_extract()

    def check_ready_to_extract(self):
        if hasattr(self, 'folder_path') and self.metadata_output_folder:
            self.extract_metadata_button.config(state=tk.NORMAL)

    def extract_metadata_from_folder(self):
        try:
            extract_metadata(self.folder_path, self.metadata_output_folder)
            self.message_label.config(text="Metadata extraction completed.", foreground="green")
            self.open_output_directory_button.config(state=tk.NORMAL)  # Enable button to open folder
        except Exception as e:
            self.message_label.config(text=f"Error: {e}", foreground="red")

    def open_metadata_output_directory(self):
        if self.metadata_output_folder:
            try:
                if platform.system() == "Windows":
                    os.startfile(self.metadata_output_folder)  # Windows
                elif platform.system() == "Darwin":
                    os.system(f'open "{self.metadata_output_folder}"')  # macOS
                elif platform.system() == "Linux":
                    os.system(f'xdg-open "{self.metadata_output_folder}"')  # Linux
            except Exception as e:
                self.message_label.config(text=f"Error opening folder: {e}", foreground="red")

    def on_extract_metadata_button_click(self):
        if hasattr(self, 'folder_path') and self.metadata_output_folder:
            self.extract_metadata_from_folder()