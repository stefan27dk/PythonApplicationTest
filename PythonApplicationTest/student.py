class student:

    def __init__(self, name, age, tlf):
        self.name = name
        self.age = age
        self.tlf = tlf



        
# Class method
    def is_over_18(self):
        if self.age <= 18:
            return False
        else:
            return True