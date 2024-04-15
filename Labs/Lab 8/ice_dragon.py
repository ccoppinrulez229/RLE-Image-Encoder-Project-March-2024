from dragon import Dragon #Dragon class is imported from dragon.py
class IceDragon (Dragon): #IceDragon class is derived from the Dragon class
    def __init__(self,name,image): #constructor creates IceDragon object with given name and image
        self.name=name
        self.image=image

    def can_breathe_fire(self): #if function is called in this specific class, it will override the Dragon class' function and return False
        return False