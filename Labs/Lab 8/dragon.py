from cow import Cow #Cow class is imported from cow.py
class Dragon (Cow): #Dragon class is derived from the Cow class
    def __init__(self,name,image): #constructor creates Dragon class with given name and image
        self.name=name
        self.image=image

    def can_breathe_fire(self): #if function is called in the default Dragon class, it will return true.
        return True