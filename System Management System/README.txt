Student Management System - Python (Tkinter + SQLite)

-------------------------------------------------------
Description:
-------------------------------------------------------
This is a basic Student Management System built with Python.
It uses:
- Tkinter for the graphical user interface (GUI)
- SQLite for storing student records
- Object-Oriented Programming (OOP) to manage student data

-------------------------------------------------------
Features:
-------------------------------------------------------
✓ Add new student records  
✓ Remove existing students by name  
✓ Update student information (e.g., phone number)  
✓ View all student records in the GUI  
✓ Input validation using a Student class

-------------------------------------------------------
Requirements:
-------------------------------------------------------
• Python 3.x  
• No external libraries required (Tkinter and SQLite are built-in)

-------------------------------------------------------
File Structure:
-------------------------------------------------------
main.py                → Entry point to launch the GUI  
gui.py                 → Contains the smsGUI class (Tkinter interface)  
student_database.py    → Handles SQLite database logic  
student.py             → Contains the Student class with validation  
student.db             → SQLite database file (auto-created)  
README.txt             → This file

-------------------------------------------------------
How to Run:
-------------------------------------------------------
1. Make sure all files are in the same directory.
2. Open a terminal or command prompt.
3. Run the app using:

   python main.py

4. Use the form to add, remove, update, and view students.

-------------------------------------------------------
Author:
-------------------------------------------------------
Harrison Labrecque

-------------------------------------------------------
Notes:
-------------------------------------------------------
• If the database file doesn't exist, it will be created automatically.
• To reset data, delete the `student.db` file and restart the app.

-------------------------------------------------------
Future:
-------------------------------------------------------
• Replace the current interface with a more modern GUI library  
  (e.g., PyQt, Kivy, or a web-based frontend using Flask or Django)

• Expand the database schema by adding new related tables:
   - Courses: to store course IDs, names, credits, and instructors  
   - Enrollments: a junction table to track which students are taking which courses  
   - Grades: to store each student’s grades per course  
   - Faculty: to manage instructors, advisors, and departments  
   - Users: for login credentials, roles (admin, student), and authentication

• Implement search and filtering (e.g., by major, GPA range, city)

• Add data export (to CSV, Excel, or PDF)

• Add user authentication and permissions (admin-only features, student logins)

• Support remote or cloud-based databases for multi-user networked access