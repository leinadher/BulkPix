import tkinter as tk
from apps.utils import main_menu, clear_window

# Create the main menu window
root = tk.Tk()
root.title("BulkPix - Menu")
root.geometry("420x240")

# Apply light theme
root.configure(bg="#F0F0F0")

# Start the main menu
main_menu(root)

# Start the GUI event loop
root.mainloop()
