import sqlite3

# Function to connect to the SQLite database
def connect():
    return sqlite3.connect("vetcare.db")

# Function to create tables if they do not exist
def create_tables():
    with connect() as conn:
        cursor = conn.cursor()

        # Owner table creation
        owner_table = """ 
        CREATE TABLE IF NOT EXISTS Owner (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name CHAR(25) NOT NULL,
            Address CHAR(25) NOT NULL,
            City CHAR(10),
            State CHAR(2),
            Zip TEXT,
            Phone VARCHAR(10)
        );
        """
        
        # Pet table creation
        pet_table = """ 
        CREATE TABLE IF NOT EXISTS Pet (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name CHAR(15) NOT NULL,
            Breed CHAR(15) NOT NULL,
            Age INT,
            OwnerID INTEGER,
            FOREIGN KEY (OwnerID) REFERENCES Owner(ID)
        );
        """
        
        # Appointment table creation
        appointment_table = """ 
        CREATE TABLE IF NOT EXISTS Appointment (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            PetID INTEGER,
            Date TEXT,
            Time TEXT,
            Description TEXT,
            FOREIGN KEY (PetID) REFERENCES Pet(ID)
        );
        """

        cursor.execute(owner_table)
        cursor.execute(pet_table)
        cursor.execute(appointment_table)
        conn.commit()

# Function to insert a new owner into the Owner table
def insert_owner(name, address, city, state, zip_code, phone):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Owner (Name, Address, City, State, Zip, Phone) VALUES (?, ?, ?, ?, ?, ?)",
            (name, address, city, state, zip_code, phone)
        )
        conn.commit()
        return cursor.lastrowid  # Return the ID of the newly inserted owner

# Function to find an owner by their name (for use when adding pets)
def find_owner_by_name(name):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Owner WHERE Name = ?", (name,))
        return cursor.fetchall()

# Function to insert a new pet into the Pet table
def insert_pet(name, breed, age, owner_id):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Pet (Name, Breed, Age, OwnerID) VALUES (?, ?, ?, ?)",
            (name, breed, age, owner_id)
        )
        conn.commit()

# Function to get all pets
def get_all_pets():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Pet")
        return cursor.fetchall()

# Function to get all owners
def get_all_owners():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Owner")
        return cursor.fetchall()

# Function to insert an appointment into the Appointment table
def insert_appointment(pet_id, date, time, description):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Appointment (PetID, Date, Time, Description) VALUES (?, ?, ?, ?)",
            (pet_id, date, time, description)
        )
        conn.commit()
        return cursor.lastrowid  # Return the ID of the newly inserted appointment

# Function to get all appointments for a specific pet
def get_appointments_for_pet(pet_id):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Appointment WHERE PetID = ?", (pet_id,))
        return cursor.fetchall()

# Function to get all appointments
def get_all_appointments():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Appointment")
        return cursor.fetchall()
