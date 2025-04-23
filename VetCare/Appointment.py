from Pet import Pet
from Owner import Owner
from datetime import datetime

class Appointment:
    def __init__(self, owner: Owner, pet: Pet, date_time: datetime, reason: str):
        self._owner = owner
        self._pet = pet
        self._date_time = date_time
        self._reason = reason

    # Getters
    def getOwner(self):
        return self._owner

    def getPet(self):
        return self._pet

    def getDateTime(self):
        return self._date_time

    def getReason(self):
        return self._reason

    # Setters
    def setOwner(self, owner: Owner):
        self._owner = owner

    def setPet(self, pet: Pet):
        self._pet = pet

    def setDateTime(self, date_time: datetime):
        self._date_time = date_time

    def setReason(self, reason: str):
        self._reason = reason

    def __str__(self):
        return (f"Appointment for {self._pet.getName()} (Owner: {self._owner.getName()}) "
                f"on {self._date_time.strftime('%Y-%m-%d %H:%M')} - Reason: {self._reason}")
