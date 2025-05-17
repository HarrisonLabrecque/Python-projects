class Student:
    def __init__(self, name, major, gpa, phone, address, city, state, zipCode):
        self._name = name
        self._major = major
        self._gpa = gpa
        self._phone = phone
        self._address = address
        self._city = city
        self._state = state
        self._zipCode = zipCode

    # Getters (accessors)
    def get_name(self):
        return self._name

    def get_major(self):
        return self._major

    def get_gpa(self):
        return self._gpa

    def get_phone(self):
        return self._phone

    def get_address(self):
        return self._address

    def get_city(self):
        return self._city

    def get_state(self):
        return self._state

    def get_zipCode(self):
        return self._zipCode

    # Setters (mutators)
    def set_name(self, name):
        self._name = name

    def set_major(self, major):
        self._major = major

    def set_gpa(self, gpa):
        if 0 <= gpa <= 4:  # Ensure GPA is within valid range
            self._gpa = gpa
        else:
            print("Invalid GPA! Must be between 0 and 4.")

    def set_phone(self, phone):
        self._phone = phone

    def set_address(self, address):
        self._address = address

    def set_city(self, city):
        self._city = city

    def set_state(self, state):
        self._state = state

    def set_zipCode(self, zipCode):
        self._zipCode = zipCode
