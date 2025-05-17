import sqlite3

class StudentDB:
    def __init__(self,db_name="students.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()

    
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            gpa INTEGER NOT NULL,
            major TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            state TEXT NOT NULL,
            zipCode INTEGER NOT NULL

        )
        """
        self.conn.execute(query)
        self.conn.commit()
    
    def add_student(self, name, gpa, major, phone, address, city, state, zipCode):
        query = """
        INSERT INTO students (name, gpa, major, phone, address, city, state, zipCode)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.conn.execute(query, (name, gpa, major, phone, address, city, state, zipCode))
        self.conn.commit()

    def search_for_student(self, field, value):
        cursor = self.conn.cursor()
        # Prevent SQL injection by allowing only specific column names
        allowed_fields = {"name", "major", "phone", "city", "state", "zipCode"}
        if field not in allowed_fields:
            raise ValueError("Invalid search field.")

        query = f"SELECT * FROM students WHERE {field} = ?"
        cursor.execute(query, (value,))
        return cursor.fetchall()
    
    def remove_student(self, field, value):
        try:
            cursor = self.conn.cursor()
        
            # Validate the search field
            allowed_fields = {"name", "major", "phone", "city", "state", "zipCode"}
            if field not in allowed_fields:
                raise ValueError("Invalid search field.")
        
            # Construct DELETE query
            delete_query = f"DELETE FROM students WHERE {field} = ?"
        
            # Execute the query
            cursor.execute(delete_query, (value,))
        
            # Commit the changes to the database
            self.conn.commit()
        
            # Close the cursor
            cursor.close()
    
        except sqlite3.Error as error:
            print("Failed to delete record from sqlite table", error)

    def update_student(self, field, value, identifier_field, identifier_value):
        try:
            cursor = self.conn.cursor()
        
            # Validate the search fields
            allowed_fields = {"name", "major", "phone", "city", "state", "zipCode"}
            if field not in allowed_fields:
                raise ValueError("Invalid field to update.")
        
            # The field used to identify the student (e.g., id, name, etc.)
            allowed_identifiers = {"id", "name", "phone"}
            if identifier_field not in allowed_identifiers:
                raise ValueError("Invalid identifier field.")
        
            # Construct UPDATE query with a WHERE clause
            update_query = f"UPDATE students SET {field} = ? WHERE {identifier_field} = ?"
        
            # Execute the query with both the new value and the identifier
            cursor.execute(update_query, (value, identifier_value))
        
            # Commit the changes to the database
            self.conn.commit()
        
            # Close the cursor
            cursor.close()

        except sqlite3.Error as error:
            print("Unable to update the table:", error)


    def get_all_students(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()

    def close(self):
        self.conn.close()
            