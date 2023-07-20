import tkinter as tk
from tkinter import messagebox
import json
import os

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website and username and password:
        folder_name = 'passwords'
        folder_path = os.path.join(os.getcwd(), folder_name)
        passwords_file = os.path.join(folder_path, 'passwords.json')
        
        try:
            os.mkdir(folder_path)
            messagebox.showinfo("Folder Created", f"Folder '{folder_name}' created successfully.")
        except FileExistsError:
            pass

        try:
            with open(passwords_file, 'r') as file:
                passwords = json.load(file)
        except FileNotFoundError:
            passwords = {}

        if website not in passwords:
            passwords[website] = {'username': username, 'password': password}
            with open(passwords_file, 'w') as file:
                json.dump(passwords, file)
            messagebox.showinfo("Success", "Password saved successfully.")
        else:
            messagebox.showwarning("Duplicate", "Password for this website already exists.")
    else:
        messagebox.showwarning("Incomplete", "Please fill in all fields.")

def get_password():
    website = website_entry.get()

    if website:
        folder_path = os.path.join(os.getcwd(), 'passwords')
        passwords_file = os.path.join(folder_path, 'passwords.json')
        
        try:
            with open(passwords_file, 'r') as file:
                passwords = json.load(file)
                if website in passwords:
                    username = passwords[website]['username']
                    password = passwords[website]['password']
                    messagebox.showinfo("Password", f"Website: {website}\nUsername: {username}\nPassword: {password}")
                else:
                    messagebox.showwarning("Not Found", "Password for this website not found.")
        except FileNotFoundError:
            messagebox.showwarning("Not Found", "Password for this website not found.")
    else:
        messagebox.showwarning("Incomplete", "Please enter a website.")

# Create GUI window
window = tk.Tk()
window.title("Password Manager")

# Set window icon
window.iconbitmap(r'C:\Users\roniv\Downloads\HD-wallpaper-cyber-security-cool-cyber-locked-password-phone-security-technology.ico')

# Create labels and entries
website_label = tk.Label(window, text="Website:", font=("Arial", 12, "bold"))
website_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
website_entry = tk.Entry(window, font=("Arial", 12))
website_entry.grid(row=0, column=1, padx=5, pady=5)

username_label = tk.Label(window, text="Username:", font=("Arial", 12, "bold"))
username_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
username_entry = tk.Entry(window, font=("Arial", 12))
username_entry.grid(row=1, column=1, padx=5, pady=5)

password_label = tk.Label(window, text="Password:", font=("Arial", 12, "bold"))
password_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
password_entry = tk.Entry(window, font=("Arial", 12), show="*")
password_entry.grid(row=2, column=1, padx=5, pady=5)

# Create buttons
save_button = tk.Button(window, text="Save Password", font=("Arial", 12, "bold"), command=save_password)
save_button.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

get_button = tk.Button(window, text="Get Password", font=("Arial", 12, "bold"), command=get_password)
get_button.grid(row=3, column=1, padx=5, pady=5, sticky=tk.E)

# Configure grid weights for resizing
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# Set window size and position
window.geometry("400x200")  # Set the desired width and height
window.update_idletasks()  # Apply any pending geometry changes
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window.winfo_width()) // 2
y = (screen_height - window.winfo_height()) // 2
window.geometry(f"+{x}+{y}")  # Center the window on the screen

# Run the GUI event loop
window.mainloop()
