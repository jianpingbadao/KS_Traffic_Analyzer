# First GUI to open a window
a = 600
b = 300
# Import stuff here
import tkinter as tk

# Create instance
win = tk.Tk()

# Add a title for our GUI
win.title("Our first GUI")

# How to make window non-resizable
# win.resizable(False, False)

# Set default size of window, still resizable 
# Window size can be initiated with variables instead of hardcoded
win.geometry("%dx%d"%(a,b)) # Width x Height






# Start the GUI/create the main loop
win.mainloop()