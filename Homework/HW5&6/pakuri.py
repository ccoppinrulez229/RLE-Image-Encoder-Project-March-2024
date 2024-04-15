class Pakuri:
    def __init__(self,species): #constructor function initializes the species, attack defense and speed variables for the class object
        self.species=species
        self.attack=(len(species)*7)+9
        self.defense=(len(species)*5)+17
        self.speed=(len(species)*6)+13

    def get_species(self): #returns the species of the critter
        return self.species

    def get_attack(self): #returns the attack value of the critter
        return self.attack

    def get_defense(self): #returns the defense value of the critter
        return self.defense

    def get_speed(self): #returns the speed of the critter
        return self.speed

    def set_attack(self,new_attack): #changes the attack value of the critter to new_attack
        self.attack=new_attack

    def evolve(self): #evolves the critter, doubling its attack, quadrupling its defense and tripling its speed
        self.set_attack(self.attack*2)
        self.defense*=4
        self.speed*=3