class Pet:
    def __init__(self,name:str,breed:str, age:int):
        self._name = name
        self._breed = breed
        self._age = age
    
    #getter methods
    def getName(self):
        return self._name
    
    def getBreed(self):
        return self._breed

    def getAge(self):
        return self._age

    #setter method
    def setName(self,name):
        self._name = name
    
    def setBreed(self,breed):
        self._breed = breed
    
    def setAge(self,age):
        self._age = age
    
    