class Owner:
    def __init__(self, name: str, address: str, city: str, state: str, zip: int, phone: str, pet: list):
        self._name = name
        self._address = address
        self._city = city
        self._state = state
        self._zip = zip
        self._phone = phone
        self._pet = pet

    # Getter methods
    def getName(self):
        return self._name

    def getAddress(self):
        return self._address

    def getCity(self):
        return self._city

    def getState(self):
        return self._state

    def getZip(self):
        return self._zip

    def getPhone(self):
        return self._phone

    def getPet(self):
        return self._pet

    # Setter methods
    def setName(self, name):
        self._name = name

    def setAddress(self, address):
        self._address = address

    def setCity(self, city):
        self._city = city

    def setState(self, state):
        self._state = state

    def setZip(self, zip):
        self._zip = zip

    def setPhone(self, phone):
        self._phone = phone

    def setPet(self, pet):
        self._pet = pet
