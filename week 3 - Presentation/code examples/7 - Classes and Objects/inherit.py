

#
#
#     Object Oritented Programming Example
#
#     An Example of Inheritance
#
#   Scenrio - Simple game with players and transportation for the players
#
#   Transportation can be a Rocket, Car, Horse, Helecopter or boat
#   Each has different qualities but they all have a speed and a max capacity of how
#   many people can fit in it.
#
#   They all share similar qualities
#
#

import random

class Transportation():
    maxcapacity = 0;
    speed = 0;
    durability = 0;

    def __init__ (self,maxcapacity,speed,durability):
        # abletouse = True; # is a player able to use this transportation
        self.maxcapacity = maxcapacity;
        self.speed = speed;
        self.durability = durability;
        return;

class Horse(Transportation):

    transportname = "Horse"
    healthpoints = 1800;

    def Move(self):
        if self.healthpoints <= 0:
            print("Horse is dead")
        else:
            print("Horse Moved")
        return;

    def FeedHorse(self):
        self.healthpoints += 25;
        return;


class Helicopter(Transportation):

    transportname = "Helicopter";
    fuel = 1000;

    # a helecoper could move up unlike a horse
    # this could be a difference between the helecopter class and the horse class
    def Move(self):
        if self.fuel <= 0:
            print("Helicopter is out of fuel")
        else:
            print("Helicopter Moved")

        return;

    def AddFuel(self):
        self.fuel += 300;
        return;




def main():

    horse1 = Horse(2,35,38);



    helecopter1 = Helicopter(6,200,500);


    horse1.Move();

    horse1.healthpoints = 0;

    horse1.Move();



    helecopter1.Move();

    helecopter1.fuel = 0;

    helecopter1.Move();


    return;


main();
