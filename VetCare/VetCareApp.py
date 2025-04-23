import db_functions as db
from datetime import datetime

# Function to display the menu options
def show_menu():
    print("\n--- VetCare System ---")
    print("1. Add New Owner")
    print("2. Add New Pet")
    print("3. View All Owners and Pets")
    print("4. Schedule an Appointment")
    print("5. Update Owner/Pet")
    print("6. Delete Owner/Pet")
    print("7. Exit")
    return input("Please select an option: ")

# Function to add a new owner
def add_owner():
    print("\n--- Add New Owner ---")
    name = input("Enter owner name: ")
    address = input("Enter address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    zip_code = input("Enter zip code: ")

    # Ensuring phone number is numeric and has the correct length (10 digits)
    while True:
        phone = input("Enter phone number (10 digits): ")
        if phone.isdigit() and len(phone) == 10:
            break
        else:
            print("Invalid phone number! Please enter exactly 10 digits.")
    
    # Insert the owner into the database
    try:
        owner_id = db.insert_owner(name, address, city, state, zip_code, phone)
        print(f"Owner {name} added successfully with ID {owner_id}.")
    except Exception as e:
        print(f"Error adding owner: {e}")

# Function to add a new pet
def add_pet():
    print("\n--- Add New Pet ---")
    owner_name = input("Enter the owner's name: ")
    owner = db.find_owner_by_name(owner_name)
    if owner:
        owner_id = owner[0][0]  # Assuming the first field is the ID
        pet_name = input("Enter pet name: ")
        breed = input("Enter pet breed: ")
        age = int(input("Enter pet age: "))
        db.insert_pet(pet_name, breed, age, owner_id)
        print(f"Pet {pet_name} added successfully for owner {owner_name}.")
    else:
        print("Owner not found!")

# Function to view all owners and pets
def view_all():
    print("\n--- View All Owners and Pets ---")
    owners = db.get_all_owners()
    if owners:
        for owner in owners:
            print(f"Owner ID: {owner[0]}, Name: {owner[1]}")
            pets = db.get_all_pets()
            for pet in pets:
                if pet[4] == owner[0]:  # Match pet owner ID to owner ID
                    print(f"  Pet ID: {pet[0]}, Name: {pet[1]}, Breed: {pet[2]}, Age: {pet[3]}")
    else:
        print("No owners found.")

# Function to schedule an appointment
def schedule_appointment():
    print("\n--- Schedule an Appointment ---")
    
    # Get the list of pets
    pets = db.get_all_pets()
    if pets:
        print("Select a pet to schedule an appointment:")
        for pet in pets:
            print(f"Pet ID: {pet[0]}, Name: {pet[1]}, Breed: {pet[2]}")
        
        pet_id = int(input("Enter pet ID for the appointment: "))
        date = input("Enter appointment date (YYYY-MM-DD): ")
        time = input("Enter appointment time (HH:MM): ")
        description = input("Enter appointment description: ")
        
        # Insert the appointment into the database
        appointment_id = db.insert_appointment(pet_id, date, time, description)
        print(f"Appointment scheduled successfully with ID {appointment_id}.")
    else:
        print("No pets found to schedule an appointment for.")

# Main function that controls the menu and user input
def main():
    # Ensure tables are created when the program starts
    db.create_tables()

    while True:
        user_choice = show_menu()
        
        if user_choice == '1':
            add_owner()
        elif user_choice == '2':
            add_pet()
        elif user_choice == '3':
            view_all()
        elif user_choice == '4':
            schedule_appointment()
        elif user_choice == '5':
            # Update details function can be added similarly
            pass
        elif user_choice == '6':
            # Delete owner/pet function can be added similarly
            pass
        elif user_choice == '7':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
