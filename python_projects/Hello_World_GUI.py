import tkinter as tk

# Function to greet user
def say_hello():
    name = name_entry.get()
    if name.strip() == "":
        greeting_label.config(text="Please enter your name!")
    else:
        greeting_label.config(text=f"Hello, {name}!")

# Main window
root = tk.Tk()
root.title("Hello World App")
root.geometry("350x200")

# Label
title_label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
title_label.pack(pady=10)

# Entry box
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack(pady=5)

# Button
greet_button = tk.Button(root, text="Greet Me", command=say_hello, font=("Arial", 12))
greet_button.pack(pady=10)

# Output label
greeting_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
greeting_label.pack(pady=10)

# Run loop
root.mainloop()
