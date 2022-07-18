#
#
#   Example of 2 classes
#  1 Player class and 1 weapon class
#
# The player can store a weapon
# The player also has health and can be effected by annother players weapon
#
#
#
#
#

import random
import os



class Weapon:

    name = "";
    description = "";
    projectile = False;
    range = 0;
    damage = 0;

    def __init__(self,name,description,projectile,range,damage):
        self.name = name;
        self.description = description;
        self.projectile = projectile;
        self.range = range;
        self.damage = damage;
        return;

    # get random damage from a weapon
    def RollForAttackDamage(self):
        attackdmg = random.randint(0,self.damage);
        return attackdmg;


class Player:

    username = "";
    healthpoints = 1000;

    def __init__(self,username):
        self.username = username;
        self.primaryweapon = Weapon("Fists","For Punching",False,0,3);
        return;

    def GetDisplayName():
        namecolor = "";
        if healthpoints < 500:
            namecolor = "red";
        else:
            namecolor = "green";
        return '<div style="color:' + namecolor + ';display-inline;"></>';

    def AssignWeapon(self,weaponobj):
        self.primaryweapon = weaponobj;
        return;

    # method for calculating percent of health
    def CalcHealthPercent(self):
        return int((self.healthpoints / 100) * 10);






#

def main():

    print("")

    # Create a player and assign it a weapon
    player1 = Player("-Thomas_292-");
    newweapon = Weapon("Sword","Iorn Long Sword",False,12,780);
    player1.AssignWeapon(newweapon);
    print("Player ("  + player1.username + ") has been given a " + newweapon.name);
    print("")

    player2 = Player("0-jhonny_pro");
    newweapon = Weapon("Cross Bow","Easy to use cross bow",True,138,450);
    player2.AssignWeapon(newweapon);
    print("Player ("  + player2.username + ") has been given a " + newweapon.name);
    print("")
    print("")


    print("Player (" + player1.username + ") will attack")
    attackdmg = player1.primaryweapon.RollForAttackDamage();
    if attackdmg == 0:
        print(" > Players attack missed...")
    else:
        print(" > Player attacked with " + str(attackdmg) + " hit points")
        player2.healthpoints -= attackdmg;

    print("")
    print("Player " + player2.username + " now has " + str(player2.CalcHealthPercent())  + "% health")

    print("")
    print("")

    # ----------------------------------------

    army = [];

    newplayer = Player("Soldier-" + str(i));
    newweapon = Weapon("Long Bow","Powerful long bow",False,400,680);

    for i in range(0,40):
        newplayer.AssignWeapon(newweapon);
        army.append(newplayer);



    return;


main();
