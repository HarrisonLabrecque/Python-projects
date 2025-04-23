VetCare System
The VetCare System is a simple command-line application built to manage pet owners, pets, and their appointments. It allows users to:

Add new owners and their pets

Schedule appointments for pets

View all owners and pets in the system

Manage appointments for pets

This project uses SQLite to store the data and provides functions to interact with the database.

Features
Owner Management: Add new owners with their name, address, phone number, and more.

Pet Management: Add new pets, link them to their owners, and manage their details.

Appointment Scheduling: Schedule appointments for pets, including the date, time, and description.

View All Data: View a list of all owners and pets, and check the scheduled appointments.

Requirements
Python 3.x

SQLite3 (comes built-in with Python)

Usage
When you run the application, you will be presented with a menu of options to choose from. The available options are:

Add New Owner: Add a new pet owner to the system.

Add New Pet: Add a new pet and link it to an existing owner.

View All Owners and Pets: Display a list of all owners and their associated pets.

Schedule an Appointment: Schedule an appointment for a pet.

Update Owner/Pet: Modify details of an existing owner or pet.

Delete Owner/Pet: Remove an owner or pet from the system.

Exit: Close the application.

Database Structure
The database consists of the following tables:

Owner Table:

Column Name	Data Type	Description
ID	INTEGER	Primary key (auto-increment)
Name	TEXT	Name of the owner
Address	TEXT	Address of the owner
City	TEXT	City where the owner lives
State	TEXT	State of the owner
Zip	TEXT	Zip code of the owner
Phone	TEXT	Phone number of the owner
Pet Table:

Column Name	Data Type	Description
ID	INTEGER	Primary key (auto-increment)
Name	TEXT	Name of the pet
Breed	TEXT	Breed of the pet
Age	INTEGER	Age of the pet
OwnerID	INTEGER	Foreign key referencing the Owner ID
Appointment Table:

Column Name	Data Type	Description
ID	INTEGER	Primary key (auto-increment)
PetID	INTEGER	Foreign key referencing the Pet ID
Date	TEXT	Date of the appointment
Time	TEXT	Time of the appointment
Description	TEXT	Description of the appointment
Example Flow
Add Owner: The user inputs owner details such as name, address, phone number, etc.

Add Pet: After adding an owner, the user can add a pet by selecting the owner's name and entering the pet’s details (name, breed, age).

Schedule Appointment: The user selects a pet and schedules an appointment by entering the date, time, and description of the appointment.

View All: The user can view all owners and pets in the system, along with scheduled appointments for each pet.