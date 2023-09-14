import tkinter as tk
from tkinter import messagebox, simpledialog, ttk


class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class ContactManager(tk.Tk):
    def __init__(self):
        super().__init__()

        self.contacts = []

        self.title("Contact Manager")
        self.geometry("400x300")

        ttk.Label(self, text="Contact Manager", font=("Arial", 24)).pack(pady=20)

        ttk.Button(self, text="Add Contact", command=self.add_contact).pack(pady=10)
        ttk.Button(self, text="View Contacts", command=self.view_contacts).pack(pady=10)
        ttk.Button(self, text="Search Contact", command=self.search_contact).pack(pady=10)
        ttk.Button(self, text="Update Contact", command=self.update_contact).pack(pady=10)
        ttk.Button(self, text="Delete Contact", command=self.delete_contact).pack(pady=10)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter Contact Name")
        phone = simpledialog.askstring("Input", "Enter Phone Number")
        email = simpledialog.askstring("Input", "Enter Email")
        address = simpledialog.askstring("Input", "Enter Address")

        if name and phone and email and address:
            self.contacts.append(Contact(name, phone, email, address))
            messagebox.showinfo("Success", "Contact added successfully!")

    def view_contacts(self):
        contacts_win = tk.Toplevel(self)
        contacts_win.title("View Contacts")

        for idx, contact in enumerate(self.contacts):
            ttk.Label(contacts_win, text=f"Name: {contact.name}, Phone: {contact.phone}").pack(pady=10)

    def search_contact(self):
        query = simpledialog.askstring("Search", "Enter name or phone to search")
        contacts_found = [contact for contact in self.contacts if query in (contact.name, contact.phone)]

        search_win = tk.Toplevel(self)
        search_win.title("Search Results")

        for contact in contacts_found:
            ttk.Label(search_win, text=f"Name: {contact.name}, Phone: {contact.phone}").pack(pady=10)

    def update_contact(self):
        name_to_update = simpledialog.askstring("Update", "Enter name of the contact to update")
        contact_to_update = next((contact for contact in self.contacts if contact.name == name_to_update), None)

        if not contact_to_update:
            messagebox.showerror("Error", "Contact not found!")
            return

        contact_to_update.phone = simpledialog.askstring("Update", "Enter new phone number", initialvalue=contact_to_update.phone)
        contact_to_update.email = simpledialog.askstring("Update", "Enter new email", initialvalue=contact_to_update.email)
        contact_to_update.address = simpledialog.askstring("Update", "Enter new address", initialvalue=contact_to_update.address)

    def delete_contact(self):
        name_to_delete = simpledialog.askstring("Delete", "Enter name of the contact to delete")
        contact_to_delete = next((contact for contact in self.contacts if contact.name == name_to_delete), None)

        if not contact_to_delete:
            messagebox.showerror("Error", "Contact not found!")
            return

        self.contacts.remove(contact_to_delete)
        messagebox.showinfo("Success", "Contact deleted successfully!")


if __name__ == "__main__":
    app = ContactManager()
    app.mainloop()
