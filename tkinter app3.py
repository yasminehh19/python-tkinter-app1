import tkinter as tk

# Function to draw a circle on the canvas
def draw_circle():
    # Create an oval with the given coordinates on the canvas
    canvas.create_oval(190, 190, 210, 210)

# Create the main window
root = tk.Tk()

# Create a canvas widget and add it to the main window
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Create a button widget and add it to the main window
button = tk.Button(root, text="Draw Circle", command=draw_circle)
button.pack()

# Start the main loop of the program
root.mainloop()