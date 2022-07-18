
'''

Example - Dog class and Dog objects

 - Each dog is unique

 - But all Dogs have shared qualites that make them dogs



'''


import time


class Dog:

    name = "";
    color = "";
    age = 0;
    happylevel = 50;

    def __init__(self,dogname,dogcolor,dogage):
        self.name = dogname;
        self.color = dogcolor;
        self.age = dogage;

    def GiveBellyRub(self):
        print(self.name + " was given a belly rub")
        self.happylevel += 10;
        return;

    def HappyBirthday(self):
        print(self.name + " had a happy birthday")
        self.age += 1;
        return;

    def DisplayDogInformation(self):
        print("")
        print("Name: " + self.name)
        print("Color: " + self.color)
        print("Age: " + str(self.age))
        print("Happy Level: " + str(self.happylevel))
        return;



#
# Example of using the class
#
#
# The class is used to create objects that are loaded in to memmory
#
#


print("")
print("------------")

print("Creating 2 dog objects")

dog1 = Dog("chester","spotted brown and white",5);
dog2 = Dog("slowpoke","tan", 5);


print("------------")
dog1.GiveBellyRub()
dog1.GiveBellyRub();

dog1.DisplayDogInformation();

print("------------")

dog2.GiveBellyRub();
dog2.HappyBirthday();
dog2.DisplayDogInformation();


print("------------")
print("")
