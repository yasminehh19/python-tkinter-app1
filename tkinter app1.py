# Import the tkinter module and the random module
from tkinter import *
import random

# Define a list of colors
colors = ['red','blue','green','yellow','orange','purple','cyan']

# Create a Tkinter root window
root = Tk()

# Set the size of the root window
root.geometry("400x400")

# Set the title of the root window
root.title("My First App ")

# Create a label widget for the button
button = Label(root,text = "Learning Buttons").pack() 

# Create another label widget for the instructions
like = Label(root,
            text = "click to change colour")
like.pack()

# Define a function to change the background color of the root window
def click():
    root.config(bg=random.choice(colors))

# Create a button widget that calls the click function when clicked
submit = Button(root,
               text = 'click',
               command = click)
submit.pack()

# Run the Tkinter event loop to display the window
root.mainloop()
