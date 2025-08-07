import tkinter as tk
from tkinter import messagebox
import json
import os

filename = "contacts.json"

# Load and save helpers
def load_contacts():
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(filename, 'w') as f:
        json.dump(contacts, f)

# Add contact
def add_contact():
    name = name_entry.get()
    number = number_entry.get()
    if name and number:
        contacts = load_contacts()
        contacts[name] = number
        save_contacts(contacts)
        update_contact_list()
        name_entry.delete(0, tk.END)
        number_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Missing Info", "Name and number required.")

# View contacts
def update_contact_list():
    contact_list.delete(0, tk.END)
    contacts = load_contacts()
    for name, number in contacts.items():
        contact_list.insert(tk.END, f"{name}: {number}")

# Delete contact
def delete_contact():
    selected = contact_list.curselection()
    if selected:
        name_number = contact_list.get(selected[0])
        name = name_number.split(":")[0].strip()
        contacts = load_contacts()
        if name in contacts:
            del contacts[name]
            save_contacts(contacts)
            update_contact_list()

# UI
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x500")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Phone Number").pack()
number_entry = tk.Entry(root, width=40)
number_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Delete Selected", command=delete_contact).pack()

tk.Label(root, text="Saved Contacts").pack()
contact_list = tk.Listbox(root, width=50, height=15)
contact_list.pack()

update_contact_list()

root.mainloop()
