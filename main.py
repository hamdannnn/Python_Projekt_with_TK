from tkinter import *
from tkinter import ttk, messagebox
from db import Database

db = Database("employees.db")

#================Root Window================#
root = Tk()
root.title("Treeview Example")
root.geometry("1500x560+41+100")
root.resizable(False, False)
root.config(bg="#2c3e50")

#================Logo Frame================#
#logo = PhotoImage(file="logo_11.png")
#root.iconphoto(False, logo)
#lbl_logo = Label(root, image=logo, bg="#2c3e50")
#lbl_logo.place(x=13, y=460)

#================Entries Frame================#
entries_frame = Frame(root, bg="#2c3e50")
entries_frame.place(x=10, y=10, width=390, height=480)
title_label = Label(entries_frame, text="Mitarbeitern Eintrag", font=("Corbel", 20,), fg="#ffffff", bg="#2c3e50")
title_label.place(x=10, y=1)

#================Form Fields================#
Label(entries_frame, text="Name:", font=("Corbel", 15), fg="#ffffff", bg="#2c3e50").place(x=10, y=48)
txtName = Entry(entries_frame, font=("Corbel", 15))
txtName.place(x=120, y=50)

Label(entries_frame, text="Job:", font=("Corbel", 15), fg="#ffffff", bg="#2c3e50").place(x=10, y=90)
txtJob = Entry(entries_frame, font=("Corbel", 15))
txtJob.place(x=120, y=90)

Label(entries_frame, text="Geschlecht:", font=("Corbel", 15), fg="#ffffff", bg="#2c3e50").place(x=10, y=130)
comboGender = ttk.Combobox(entries_frame, width=18, font=("Corbel", 15), state="readonly")
comboGender['values'] = ("Männlich", "Weiblich")
comboGender.place(x=120, y=130)
comboGender.current(0)

Label(entries_frame, text="Alter:", font=("Corbel", 15), fg="#ffffff", bg="#2c3e50").place(x=10, y=170)
txtAge = Entry(entries_frame, font=("Corbel", 15))
txtAge.place(x=120, y=170)

Label(entries_frame, text="Email:", font=("Corbel", 15), fg="#ffffff", bg="#2c3e50").place(x=10, y=210)
txtEmail = Entry(entries_frame, font=("Corbel", 15))
txtEmail.place(x=120, y=210)

Label(entries_frame, text="Telefon:", font=("Corbel", 15), fg="#ffffff", bg="#2c3e50").place(x=10, y=250)
txtPhone = Entry(entries_frame, font=("Corbel", 15))
txtPhone.place(x=120, y=250)

Label(entries_frame, text="Adresse:", font=("Corbel", 15), fg="#ffffff", bg="#2c3e50").place(x=10, y=290)
txtAddress = Entry(entries_frame, font=("Corbel", 15))
txtAddress.place(x=120, y=290, width=204, height=70)

#================Function to fetch data================#
def load_data():
    for row in treeview.get_children():
        treeview.delete(row)
    for row in db.fetch_all_employees():
        treeview.insert("", END, values=row)

#================Function to Add================#
def add_data():
    if txtName.get() == "" or txtJob.get() == "":
        messagebox.showerror("Fehler", "Bitte alle Felder ausfüllen")
        return
    db.insert_employee(txtName.get(), txtJob.get(), comboGender.get(), int(txtAge.get()), txtEmail.get(), txtPhone.get(), txtAddress.get())
    load_data()
    clear_fields()

#================Function to Update================#
def update_data():
    selected = treeview.focus()
    if not selected:
        messagebox.showerror("Fehler", "Bitte wählen Sie einen Eintrag zum Aktualisieren aus")
        return
    values = treeview.item(selected, 'values')
    emp_id = values[0]
    db.update_employee(emp_id, txtName.get(), txtJob.get(), comboGender.get(), int(txtAge.get()), txtEmail.get(), txtPhone.get(), txtAddress.get())
    load_data()
    clear_fields()

#================Function to Delete================#
def delete_data():
    selected = treeview.focus()
    if not selected:
        messagebox.showerror("Fehler", "Bitte wählen Sie einen Eintrag zum Löschen aus")
        return
    values = treeview.item(selected, 'values')
    emp_id = values[0]
    db.delete_employee(emp_id)
    load_data()
    clear_fields()

#================Function to Fill Fields================#
def fill_fields(event):
    selected = treeview.focus()
    values = treeview.item(selected, 'values')
    if values:
        txtName.delete(0, END); txtName.insert(0, values[1])
        txtJob.delete(0, END); txtJob.insert(0, values[2])
        comboGender.set(values[3])
        txtAge.delete(0, END); txtAge.insert(0, values[4])
        txtEmail.delete(0, END); txtEmail.insert(0, values[5])
        txtPhone.delete(0, END); txtPhone.insert(0, values[6])
        txtAddress.delete(0, END); txtAddress.insert(0, values[7])

#================Clear Fields================#
def clear_fields():
    txtName.delete(0, END)
    txtJob.delete(0, END)
    comboGender.current(0)
    txtAge.delete(0, END)
    txtEmail.delete(0, END)
    txtPhone.delete(0, END)
    txtAddress.delete(0, END)

#================Buttons================#
Button(entries_frame, text="Hinzufügen", command=add_data, font=("Corbel", 15), bg="#27ae60", fg="#ffffff").place(x=10, y=380, width=120, height=40)
Button(entries_frame, text="Aktualisieren", command=update_data, font=("Corbel", 15), bg="#2980b9", fg="#ffffff").place(x=140, y=380, width=120, height=40)
Button(entries_frame, text="Löschen", command=delete_data, font=("Corbel", 15), bg="#c0392b", fg="#ffffff").place(x=270, y=380, width=120, height=40)

#  Button, etwas nach unten verschoben (unter die anderen):
Button(entries_frame, text="Anzeigen", command=load_data, font=("Corbel", 15), bg="#f39c12", fg="#ffffff").place(x=10, y=430, width=380, height=40)

#================Treeview================#
treeview_frame = Frame(root, bg="#2c3e50")
treeview_frame.place(x=410, y=20, width=1100, height=470)

treeview = ttk.Treeview(treeview_frame, columns=("ID", "Name", "Job", "Geschlecht", "Age", "Email", "Telefon", "Adresse"), show="headings")
treeview.heading("ID", text="ID")
treeview.column("ID", width=40)
treeview.heading("Name", text="Name")
treeview.column("Name", width=120)
treeview.heading("Job", text="Job")
treeview.column("Job", width=120)
treeview.heading("Geschlecht", text="Geschlecht")
treeview.column("Geschlecht", width=90)
treeview.heading("Age", text="Alter")
treeview.column("Age", width=80)
treeview.heading("Email", text="Email")
treeview.column("Email", width=160)
treeview.heading("Telefon", text="Telefon")
treeview.column("Telefon", width=120)
treeview.heading("Adresse", text="Adresse")
treeview.column("Adresse", width=200)
treeview.bind("<ButtonRelease-1>", fill_fields)
treeview.place(x=10, y=10, width=1040, height=470)

scrollbar = Scrollbar(treeview_frame, orient=VERTICAL, command=treeview.yview)
scrollbar.place(x=1040, y=10, height=470)
treeview.configure(yscrollcommand=scrollbar.set)

#================Start mit Daten laden================#
load_data()
root.mainloop()
