import tkinter as tk

# Create a function to be called when the submit button is pressed
def submit_form():
    # Get the values entered by the user in the entry widgets
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password are correct (for demonstration purposes, just hardcode a check for username and password)
    if username == "admin" and password == "password":
        # Change the background color of the window to orange
        root.config(bg="orange")

        # Create a welcome message with the username in bold and comic sans font
        welcome_message = tk.Label(root, text=f"Welcome {username}!", font=("Comic Sans MS", 16, "bold"))
        welcome_message.pack()
    else:
        # If the username or password is incorrect, show an error message
        error_message = tk.Label(root, text="Incorrect username or password", fg="red")
        error_message.pack()

# Create the main window
root = tk.Tk()
root.title("Login Form")

# Create the username label and entry widget
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create the password label and entry widget
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*") # Use the show option to hide the password
password_entry.pack()

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

# Start the main event loop
root.mainloop()
