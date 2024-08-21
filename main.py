import tkinter as tk
from apps.utils import main_menu, clear_window

# Create the main menu window
root = tk.Tk()
root.title("BulkPix")
root.geometry("420x280")

# Start the main menu
main_menu(root)

# Start the GUI event loop
root.mainloop()