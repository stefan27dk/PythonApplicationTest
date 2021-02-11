#Inheritance Import Class
from Chef import Chef

#Using Inheritance "Chef"
class ChineseChef(Chef):

    def make_fried_rice(self):
        print("China - making rice")

     # Overriding the inherited method   
    def make_special_dish(self):
        print("Orange Chicken")