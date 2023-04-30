# made by https://github.com/Stina0081
import random
import string
import tkinter as tk
import pyperclip

class PasswordGenerator:
    
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")
        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)
        self.length_entry = tk.Entry(master, width=5)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)
        self.strength_label = tk.Label(master, text="Password Strength:")
        self.strength_label.grid(row=1, column=0, padx=10, pady=10)
        self.strength_var = tk.StringVar()
        self.strength_var.set("medium")
        self.strength_menu = tk.OptionMenu(master, self.strength_var, "weak", "medium", "strong")
        self.strength_menu.grid(row=1, column=1, padx=10, pady=10)
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.password_label = tk.Label(master, text="")
        self.password_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_password)
        self.copy_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self):

        password_length = int(self.length_entry.get())
        password_strength = self.strength_var.get()
        if password_strength == "weak":
            characters = string.digits
        elif password_strength == "medium":
            characters = string.ascii_letters + string.digits
        elif password_strength == "strong":
            characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for i in range(password_length))
        self.password_label.config(text=password)
        pyperclip.copy(password)
    def copy_password(self):
        password = self.password_label.cget("text")
        pyperclip.copy(password)
root = tk.Tk()
app = PasswordGenerator(root)
root.mainloop()
