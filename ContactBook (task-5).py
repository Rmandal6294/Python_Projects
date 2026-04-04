import tkinter as tk
from tkinter import messagebox

contact_Book = []

def view_Contacts():
    contactBox.delete(0, tk.END)
    i = 1
    for contact in contact_Book:
        contactBox.insert(tk.END, f"{i}. {contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")
        i += 1
        
def add_Contact():
    name = user_name.get()
    phoneNumber = phone_number.get()
    email = user_email.get()
    address = user_address.get()
    
    if not name.strip() or not phoneNumber.strip() or not email.strip() or not address.strip():
        messagebox.showwarning("Warning", "!Empty field Detect.")
        return
    
    contact_Book.append({
        "name": name,
        "phone": phoneNumber,
        "email": email,
        "address": address
    })
    clearInputFields()
    contactBox.delete(0, tk.END)
    contactBox.insert(tk.END,f" Contact {name} add on Contact Book Successfully")
    
    
def searchByPhoneNumber():
    searchNumber = phone_number.get()
    contactBox.delete(0, tk.END)
    
    if searchNumber.strip() == "":
        messagebox.showwarning("Warning", "! Empty Field Detect")
        return
    
    found = False
    for search in contact_Book:
        if searchNumber in search["phone"]:
            contactBox.insert(tk.END, f"{search['name']} - {search['phone']} - {search['email']} - {search['address']}")
            found = True
            
    if not found:
        contactBox.insert(tk.END, "No Record Found")
            
def updateContact():
    try:
        index = contactBox.curselection()[0]
    except Exception:
        messagebox.showerror("Error", "At First Select An Contact")
        return
    
    name = user_name.get()
    phoneNumber = phone_number.get()
    email = user_email.get()
    address = user_address.get()
    
    if not name.strip() or not phoneNumber.strip() or not email.strip() or not address.strip():
        messagebox.showwarning("Warning", "!Empty field Detect.")
        return
    BeforeName = contact_Book[index]['name'] 
    contact_Book[index] = {
        "name": name,
        "phone": phoneNumber,
        "email": email,
        "address": address
    }
    clearInputFields()
    contactBox.delete(0, tk.END)
    contactBox.insert(tk.END,f" Contact {BeforeName} Update to {name}  Successfully")
    
def deleteContact():
    try:
        index = contactBox.curselection()[0]
    except Exception:
        messagebox.showerror("Error", "At First Select An Contact")
        return
    
    BeforeName = contact_Book[index]['name'] 
    contact_Book.pop(index)
    contactBox.delete(0, tk.END)
    contactBox.insert(tk.END,f" Contact {BeforeName} Deleted Successfully")
    
def clearInputFields():
    user_name.delete(0, tk.END)
    phone_number.delete(0, tk.END)
    user_email.delete(0, tk.END)
    user_address.delete(0, tk.END)
    
contact_app = tk.Tk()
contact_app.title("Contact Book")
contact_app.config(bg="lightgreen")

tk.Label(contact_app, text= "📔 Contact Book 📔", font=("Georgia", 20, "bold"), bg="gold", fg="white", width=100,).pack(pady=0)

tk.Label(contact_app, text="""
👇 INSTRUCTIONS: ⬇\n
1.) For view all contacts Click "View CONTACTS"\n
2.) For "ADD CONTACT" Fill up all of the Input Field.\n
3.) For "SEARCH CONTACT" Fill up only "Phone Number" filed.\n
4.) For "UPDATE CONTACT" at first 'View Contact' then 'Select' any contact then Fill up all of the Input Field.\n
5.) For "DELETE CONTACT" select the contact and delete\n
         """, font=("Georgia", 10, "bold"), bg="#0f1117", fg="#f0c040", justify="left").pack(pady=20)

InputFiledFrame = tk.Frame(contact_app)
InputFiledFrame.config(bg="lightgreen")
InputFiledFrame.pack(pady=30)

name_frame = tk.Frame(InputFiledFrame)
name_frame.pack(side="left", padx=8)
tk.Label(name_frame, text="Name", font=("Georgia", 10, "bold"), fg="green", ).pack()
user_name = tk.Entry(name_frame, font=("Courier", 13), fg="lime", bd=0, width=30)
user_name.pack(ipady=5)

phone_frame = tk.Frame(InputFiledFrame)
phone_frame.pack(side="left", padx=8)
tk.Label(phone_frame, text="Phone Number", font=("Georgia", 10, "bold"), fg="green").pack()
phone_number = tk.Entry(phone_frame, font=("Courier", 13), fg="lime", bd=0, width=30)
phone_number.pack(ipady=5)

email_frame = tk.Frame(InputFiledFrame)
email_frame.pack(side="left", padx=8)
tk.Label(email_frame, text="Email", font=("Georgia", 10, "bold"), fg="green").pack()
user_email = tk.Entry(email_frame, font=("Courier", 13), fg="lime", bd=0, width=30)
user_email.pack(ipady=5)

address_frame = tk.Frame(InputFiledFrame)
address_frame.pack(side="left", padx=8)
tk.Label(address_frame, text="Address", font=("Georgia", 10, "bold"), fg="green").pack()
user_address = tk.Entry(address_frame, font=("Courier", 13), fg="lime", bd=0, width=30)
user_address.pack(ipady=5)

ButtonFrame= tk.Frame(contact_app)
ButtonFrame.config(bg="lightgreen")
ButtonFrame.pack(pady=30)
tk.Button(ButtonFrame, text="View Contacts", font=("Georgia", 10, "bold"), width=20, bd = 2, bg= "gold", fg = "white", command=view_Contacts).pack(side="left", padx=10, ipady=5)
tk.Button(ButtonFrame, text="Add Contact", font=("Georgia", 10, "bold"), width=20, bd = 2, bg= "gold", fg = "white", command=add_Contact).pack(side="left", padx=10, ipady=5)
tk.Button(ButtonFrame, text="Search Contact", font=("Georgia", 10, "bold"), width=20, bd = 2, bg= "gold", fg = "white", command=searchByPhoneNumber).pack(side="left", padx=10, ipady=5)
tk.Button(ButtonFrame, text="Update Contact", font=("Georgia", 10, "bold"), width=20, bd = 2, bg= "gold", fg = "white", command=updateContact).pack(side="left", padx=10, ipady=5)
tk.Button(ButtonFrame, text="Delete Contact", font=("Georgia", 10, "bold"), width=20, bd = 2, bg= "gold", fg = "white", command=deleteContact).pack(side="left", padx=10, ipady=5)

contactBox = tk.Listbox(contact_app, font=("Georgia", 12, "bold"),  bd=0, width=100, height=15)
contactBox.pack(pady=10)

contact_app.mainloop()