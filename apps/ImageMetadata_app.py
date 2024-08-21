import tkinter as tk
from tkinter import filedialog, ttk
from scripts.ImageMetadata import extract_metadata, extract_specific_exif, metadata_to_dataframe
import os
import platform
from apps.utils import main_menu, clear_window


class ImageMetadataApp:
    def __init__(self, root):
        self.root = root
        self.metadata_output_file = None
        self.folder_path = None
        self.setup_widgets()

    def setup_widgets(self):
        # Input folder button
        self.select_folder_button = ttk.Button(self.root, text="Input folder",
                                               command=self.on_select_folder_button_click)
        self.select_folder_button.pack(padx=10, pady=10)

        # Output CSV button (Initially disabled)
        self.select_output_button = ttk.Button(self.root, text="Output CSV",
                                               command=self.on_select_output_button_click, state=tk.DISABLED)
        self.select_output_button.pack(padx=10, pady=10)

        # Open output directory button
        self.open_output_directory_button = ttk.Button(self.root, text="Open output folder",
                                                       command=self.open_metadata_output_directory, state=tk.DISABLED)
        self.open_output_directory_button.pack(padx=10, pady=10)

        # Info label
        self.message_label = ttk.Label(self.root,
                                       text="Select input folder with images and choose CSV output file.",
                                       wraplength=350)
        self.message_label.pack(pady=10)

        # Back button
        back_button = ttk.Button(self.root, text="Back", command=self.return_to_main_menu)
        back_button.pack(pady=10)

    def return_to_main_menu(self):
        clear_window(self.root)
        main_menu(self.root)

    def on_select_folder_button_click(self):
        self.folder_path = filedialog.askdirectory(title="Select Folder with Images")
        if self.folder_path:
            self.select_output_button.config(state=tk.NORMAL)  # Enable the Output CSV button
            self.try_extract_metadata()

    def on_select_output_button_click(self):
        # Ask the user to choose the output CSV file
        self.metadata_output_file = filedialog.asksaveasfilename(
            title="Select Output CSV File",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            initialfile="metadata.csv"
        )
        if self.metadata_output_file:
            self.try_extract_metadata()

    def try_extract_metadata(self):
        if self.folder_path and self.metadata_output_file:
            self.extract_metadata_from_folder()

    def extract_metadata_from_folder(self):
        try:
            # Check for valid images
            valid_images = [file for file in os.listdir(self.folder_path) if
                            file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]

            if not valid_images:
                self.message_label.config(text="Error: No valid photos found in the selected folder.", foreground="red")
                return

            # If valid images are found, proceed with metadata extraction
            extract_metadata(self.folder_path, os.path.dirname(self.metadata_output_file),
                             os.path.basename(self.metadata_output_file))
            self.message_label.config(text="Metadata extraction completed.", foreground="green")
            self.open_output_directory_button.config(state=tk.NORMAL)  # Enable button to open folder
        except Exception as e:
            self.message_label.config(text=f"Error: {e}", foreground="red")

    def open_metadata_output_directory(self):
        if self.metadata_output_file:
            try:
                output_dir = os.path.dirname(self.metadata_output_file)
                if platform.system() == "Windows":
                    os.startfile(output_dir)  # Windows
                elif platform.system() == "Darwin":
                    os.system(f'open "{output_dir}"')  # macOS
                elif platform.system() == "Linux":
                    os.system(f'xdg-open "{output_dir}"')  # Linux
            except Exception as e:
                self.message_label.config(text=f"Error opening folder: {e}", foreground="red")

