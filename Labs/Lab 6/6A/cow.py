class Cow: #Cow class is established, allowing for different iterations to be made
    def __init__(self,name): #initializes a cow object with name set to itself and image set to none
        self.name=name
        self.image=None
        pass

    def get_name(self): #Returns the name of the cow for that iteration
        return self.name
        pass

    def get_image(self): #returns the image used to display the cow in that instance
        return self.image
        pass

    def set_image(self,image): #sets the image used to display the cow
        self.image=image
        pass