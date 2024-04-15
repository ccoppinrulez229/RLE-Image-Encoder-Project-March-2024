from pakuri import Pakuri #imports Pakuri class from pakuri.

class Pakudex (Pakuri):

    def __init__(self,capacity=20): #initializes object to contain the capacity of critters specified, with default capacity being 20
        self.capacity=capacity
        self.pakudexlist = []  # pakudexlist is initialized, which is where the class objects will be stored.
        self.totalcritters = 0  # totalcritters variable initialized as 0, which will keep track of the current size of the pakudex
    def get_size(self): #returns the number of critters currently stored in the pakudex
        return self.totalcritters

    def get_capacity(self): #returns the capacity the pakudex can hold
        return self.capacity

    def add_pakuri(self,species): #adds species to pakudex list
        if len(self.pakudexlist)>0: #if the length of the pakudex list is greater than 0, look through the entire list
            for object in self.pakudexlist: #if the species is in the list, return False
                if str(object.get_species())==species:
                    return False

            #if the above loop exhausts and False is not returned, add the species to the pakudex and return True
            self.totalcritters += 1  # totalcritters increases by 1 for each successful pakuri added
            pakuri = Pakuri(species)  # initializes the species specified by the user as an object in the pakuri class
            self.pakudexlist.append(pakuri)
            return True
        else: #if the list is empty, automatically add the species to the list
            self.totalcritters += 1
            pakuri = Pakuri(species)
            self.pakudexlist.append(pakuri)
            return True

    def get_species_array(self):
        speciesstringlist=[] #speciesstringlist initialized, which will contain the string names for all the species
        if len(self.pakudexlist)>0: #if the pakudex list contains species, return the list of species strings
            for object in self.pakudexlist: #for loop goes through each object and adds the respective species to the list
                speciesstringlist.append(str(object.get_species()))
            return speciesstringlist
        else:
            return None

    def get_stats(self,species):
        if len(self.pakudexlist)>0:
            for object in self.pakudexlist: #for loop goes through entire pakudex object list to check if any object names match the species
                if str(object.get_species())==species: #if so, return statlist with attack, defense and speed of the species
                    statlist=[int(object.get_attack()),int(object.get_defense()),int(object.get_speed())]
                    return statlist
        return None #if the species is not in the list or there are no items in the pakudex list, return None

    def sort_pakuri(self): #sorts the pakudex objects
        speciesstringlist = [] #speciesstring list is initialized, which will hold the string names for all species
        newobjectlist=[] #new object list is initialized, which will hold the sorted objects
        if len(self.pakudexlist) > 0:  # if the pakudex list contains species, return the list of species strings
            for object in self.pakudexlist:  # for loop goes through each object and adds the respective name to the list
                speciesstringlist.append(str(object.get_species()))
        speciesstringlist.sort() #when above loop exhausts, sort the species strings in alphabetical order
        for obj in speciesstringlist: #for loop goes through each string in the speciesstring list and matches them accordingly with the objects
            for itm in self.pakudexlist: #if the object's species name matches the current iteration of the string, append to newobjectlist
                if str(itm.get_species())==obj:
                    newobjectlist.append(itm)
        self.pakudexlist=newobjectlist #update pakudexlist to the newly arranged list for the objects

    def evolve_species(self,species):
        if len(self.pakudexlist)>0:
            for object in self.pakudexlist: #for loop goes through entire pakudex object list to check any object names match the species
                if str(object.get_species())==species: #if so, evolve that specific object and return True
                    object.evolve()
                    return True
        return False #if the species is not in the pakudex list, return False