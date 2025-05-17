from student_database import StudentDB
from tkinter import *
from tkinter import messagebox
from student import Student

class smsGUI:
    def __init__(self, root):
        self.db = StudentDB()
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("600x600")

        self.create_menu()
        self.create_form()
        self.add_buttons()
    
    def create_menu(self):
        menubar = Menu(self.root)

        # File Menu
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.exit_menu)
        menubar.add_cascade(label="File", menu=file_menu)

        # Help Menu
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.help_menu)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

    def create_form(self):
        # Input fields
        self.entries = {}
        labels = ["Name", "GPA", "Major", "Phone", "Address", "City", "State", "ZipCode"]
        for i, label in enumerate(labels):
            Label(self.root, text=label).grid(row=i, column=0, padx=5, pady=5, sticky=W)
            entry = Entry(self.root, width=30)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[label.lower()] = entry

        self.output = Text(self.root, width=70, height=15)
        self.output.grid(row=9, column=0, columnspan=2, padx=5, pady=10)

    def add_buttons(self):
        Button(self.root, text="Add Student", command=self.add_student).grid(row=0, column=2, padx=10)
        Button(self.root, text="Remove Student", command=self.remove_student).grid(row=1, column=2, padx=10)
        Button(self.root, text="Update Student", command=self.update_student).grid(row=2, column=2, padx=10)
        Button(self.root, text="List Students", command=self.list_student).grid(row=3, column=2, padx=10)

    def help_menu(self):
        messagebox.showinfo("Help", "This is a simple student management system.")

    def exit_menu(self):
        self.root.destroy()

    def add_student(self):
        try:
            student = Student(
                self.entries["name"].get(),
                self.entries["major"].get(),
                float(self.entries["gpa"].get()),
                self.entries["phone"].get(),
                self.entries["address"].get(),
                self.entries["city"].get(),
                self.entries["state"].get(),
                int(self.entries["zipcode"].get())
            )
            self.db.add_student(
                student.get_name(), student.get_gpa(), student.get_major(),
                student.get_phone(), student.get_address(), student.get_city(),
                student.get_state(), student.get_zipCode()
            )
            messagebox.showinfo("Success", "Student added.")
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Error", f"Could not add student:\n{e}")

    def remove_student(self):
        name = self.entries["name"].get()
        if name:
            try:
                self.db.remove_student("name", name)
                messagebox.showinfo("Removed", f"Student '{name}' removed.")
                self.clear_form()
            except Exception as e:
                messagebox.showerror("Error", f"Could not remove student:\n{e}")
        else:
            messagebox.showwarning("Missing Info", "Enter name to remove.")

    def update_student(self):
        name = self.entries["name"].get()
        phone = self.entries["phone"].get()
        if name and phone:
            try:
                self.db.update_student("phone", phone, "name", name)
                messagebox.showinfo("Updated", "Phone updated for " + name)
            except Exception as e:
                messagebox.showerror("Error", f"Could not update student:\n{e}")
        else:
            messagebox.showwarning("Missing Info", "Name and new phone are required.")

    def list_student(self):
        try:
            students = self.db.get_all_students()
            self.output.delete("1.0", END)
            for student in students:
                line = f"{student[1]} | {student[2]} | {student[3]} | {student[4]}\n"
                self.output.insert(END, line)
        except Exception as e:
            messagebox.showerror("Error", f"Could not list students:\n{e}")

    def clear_form(self):
        for entry in self.entries.values():
            entry.delete(0, END)
