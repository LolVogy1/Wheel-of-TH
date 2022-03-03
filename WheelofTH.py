# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:35:35 2022

@author: AlexV
"""
import random
from enum import Enum



"""Three Houses Unit"""
class Unit:
    def __init__(self, name, end_class):
        self.name = name
        self.end_class = end_class
    
    def get_name(self):
        return self.name
    
    def get_end_class(self):
        return self.end_class


"""enum of generic endgame classes"""
class End_Class(Enum):
    swordmaster = 1
    assassin = 2
    paladin = 3
    warrior = 4
    fortress_knight = 5
    sniper = 6
    warlock = 7
    bishop = 8
    trickster = 9
    wyvern_lord = 10
    mortal_savant = 11
    great_knight = 12
    bow_knight = 13
    dark_knight = 14
    holy_knight = 15
    unique = 16
    
"""Male-only classes"""
class Male_Class(Enum):
    hero = 1
    grappler = 2
    war_monk = 3
    war_master = 4
    dark_bishop = 5
    
"""Female-only classes"""
class Female_Class(Enum):
    war_cleric = 1
    dark_flier = 2
    valkyrie = 3
    falcon_knight = 4
    gremory = 5


    
"""Maps the end_class enum to a presentable string representation"""
def class_hash(end_class):
    class_name = {}
    class_name[End_Class.swordmaster] = "Swordmaster"
    class_name[End_Class.assassin] = "Assassin"
    class_name[End_Class.paladin] = "Paladin"
    class_name[End_Class.warrior] = "Warrior"
    class_name[Male_Class.hero] = "Hero"
    class_name[End_Class.fortress_knight] = "Fortress Knight"
    class_name[End_Class.sniper] = "Sniper"
    class_name[Male_Class.grappler] = "Grappler"
    class_name[Male_Class.dark_bishop] = "Dark Bishop"
    class_name[End_Class.bishop] = "Bishop"
    class_name[End_Class.warlock] = "Warlock"
    class_name[End_Class.trickster] = "Trickster"
    class_name[Male_Class.war_monk] = "War Monk"
    class_name[Female_Class.war_cleric] = "War Cleric"
    class_name[Female_Class.dark_flier] = "Dark Flier"
    class_name[Female_Class.valkyrie] = "Valkyrie"
    class_name[Female_Class.falcon_knight] = "Falcon Knight"
    class_name[End_Class.wyvern_lord] = "Wyvern Lord"
    class_name[End_Class.mortal_savant] = "Mortal Savant"
    class_name[End_Class.great_knight] = "Great Knight"
    class_name[End_Class.bow_knight] = "Bow Knight"
    class_name[End_Class.dark_knight] = "Dark Knight"
    class_name[End_Class.holy_knight] = "Holy Knight"
    class_name[Male_Class.war_master] = "War Master"
    class_name[Female_Class.gremory] = "Gremory"
    class_name[End_Class.unique] = "Unique Class"
    return class_name[end_class]

"""Selects a random line in a text file"""
def random_line(afile):
    afile.seek(0)
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num):
            continue
        line = aline
    return line

"""Decides the endgame class of the unit"""
def get_class(gender,lord):
    if gender == "Male" or gender == "male":
        if lord =="Yes":
            class_no = random.randint(1,21)
            #generic classes
            if class_no >= 1 and class_no <=16:
                class_name = End_Class(class_no)
            #male-only classes
            else:
                class_no = random.randint(1,5)
                class_name = Male_Class(class_no)
        else:
            class_no = random.randint(1,20)
            if class_no >= 1 and class_no <=15:
                class_name = End_Class(class_no)
            else:
                class_no = random.randint(1,5)
                class_name = Male_Class(class_no)
    #cba to error check         
    else:
        if lord =="Yes":
            class_no = random.randint(1,21)
            #generic classes
            if class_no >= 1 and class_no <=16:
                class_name = End_Class(class_no)
            #female-only classes
            else:
                class_no = random.randint(1,5)
                class_name = Female_Class(class_no)
        else:
            class_no = random.randint(1,20)
            if class_no >= 1 and class_no <=15:
                class_name = End_Class(class_no)
            else:
                class_no = random.randint(1,5)
                class_name = Female_Class(class_no)
    end_class = class_hash(class_name)
    return end_class


"""Create Byleth Unit"""
def make_byleth():
    gender_num = random.randint(0,1)
    if gender_num == 0:
        gender = "Male"
        name = "Byleth (M)"
    else:
        gender = "Female"
        name = "Byleth (F)"
    end_class = get_class(gender,"Yes")
    #makes a Unit instance (name, class)
    byleth = Unit(name,end_class)
    return byleth


"""
Generates the lineup for the house
3 random units will be generated that can be recruited
"""
def generate_house(route, lineup):
    house_lineup = lineup
    counter = 0
    f = open("conditionalrecruits.txt")
    f2 = open("recruits.txt")
    '''Crimson Flower'''
    if route == 1:
        #get the lord and retainer units first
        while line := f.readline():
            unit = line.split(",")
            if unit[1] == "be":
                #generate the unit and their build
                new_unit = Unit(unit[0],get_class(unit[2],unit[3]))
                house_lineup.append(new_unit)
            #decide if we want to use Jeritza
            elif unit[0] == "Jeritza":
                jeritza = random.randint(0,100)
                if jeritza > 49:
                    new_unit = Unit(unit[0],get_class(unit[2],unit[3]))
                    house_lineup.append(new_unit)
                    counter += 1
           
            else:
                continue
        #get the rest of the house
        while line := f2.readline():
            unit = line.split(",")
            if unit[1] == "be":
                #generate the unit and their build
                new_unit = Unit(unit[0],get_class(unit[2],unit[3]))
                house_lineup.append(new_unit)
            else:
                continue
        #generate 3 random recruits
        #Hilda and certain church units cannot be recruited in CF
        while counter < 3:
            unit = random_line(f2).split(",")
            if unit[0] != "Hilda" and unit[1] != "be" and unit[1] != "chss":
                new_unit = Unit(unit[0],get_class(unit[2],unit[3]))
                house_lineup.append(new_unit)
                counter += 1
            else:
                continue
            
    '''Azure Moon'''
    if route == 2:
        #get the lord and retainer units first
        while line := f.readline():
            unit = line.split(",")
            if unit[1] == "bl":
                #generate the unit and their build
                new_unit = Unit(unit[0],get_class(unit[2],unit[3]))
                house_lineup.append(new_unit)
                    
            else:
                continue
        #get the rest of the house
        while line := f2.readline():
            unit = line.split(",")
            if unit[1] == "bl":
                #generate the unit and their build
                new_unit = Unit(unit[0],get_class(unit[2],unit[3]))
                house_lineup.append(new_unit)
            else:
                continue
        #generate 3 random recruits
        while counter < 3:
            unit = random_line(f2).split(",")
            if unit[1] != "bl":
                new_unit = Unit(unit[0],get_class(unit[2],unit[3]))
                house_lineup.append(new_unit)
                counter += 1
            else:
                continue
            
    '''Verdant Wind'''
    if route == 3:
        #get the lord and retainer units first
        while line := f.readline():
            unit = line.split(",")
            if unit[1] == "gd":
                #generate the unit and their build
                new_unit = Unit(unit[0],get_class(unit[2],unit[3]))
                house_lineup.append(new_unit)
                    
            else:
                continue
        #get the rest of the house
        while line := f2.readline():
            unit = line.split(",")
            if unit[1] == "gd":
                #generate the unit and their build
                new_unit = Unit(unit[0],get_class(unit[2],unit[3]))
                house_lineup.append(new_unit)
            else:
                continue
        #generate 3 random recruits
        while counter < 3:
            unit = random_line(f2).split(",")
            if unit[1] != "gd":
                new_unit = Unit(unit[0],get_class(unit[2],unit[3]))
                house_lineup.append(new_unit)
                counter += 1
            else:
                continue
    '''Silver Snow'''
    if route == 4:
        while line := f2.readline():
            unit = line.split(",")
            if unit[1] == "chss":
                #generate the unit and their build
                new_unit = Unit(unit[0],get_class(unit[2],unit[3]))
                house_lineup.append(new_unit)
                    
            else:
                continue
        #get the rest of the house
        f2.seek(0)
        while line := f2.readline():
            unit = line.split(",")
            if unit[1] == "be":
                #generate the unit and their build
                new_unit = Unit(unit[0],get_class(unit[2],unit[3]))
                house_lineup.append(new_unit)
            else:
                continue
        #generate 3 random recruits
        while counter < 3:
            unit = random_line(f2).split(",")
            if unit[1] != "be" and unit[1] != "chss":
                new_unit = Unit(unit[0],get_class(unit[2],unit[3]))
                house_lineup.append(new_unit)
                counter += 1
            else:
                continue
    f.close()
    f2.close()
    return house_lineup
        
            
"""
Completely randomises the lineup
Best done on NG+
"""
#def generate_randomiser():
    


"""Chooses the route"""
def choose_route(lineup):
    house_lineup = lineup
    routename =""
    route = random.randint(1,4)
    byleth = make_byleth()
    house_lineup.append(byleth)
    if route == 1:
        routename = "Crimson Flower" 
    elif route == 2:
        routename = "Azure Moon"
    elif route == 3:
        routename = "Verdant Wind"
    elif route == 4:
        routename = "Silver Snow"
    print("Your route is:",routename)
    full_lineup = generate_house(route, house_lineup)
    counter = 1
    for unit in full_lineup:
        print("unit "+str(counter)+":"+str(unit.name)+" Class: "+str(unit.end_class))
        counter +=1
        
    

if __name__ == "__main__":
    print("Welcome to the Wheel of Three Houses!")
    house_lineup = []
    choose_route(house_lineup)
    
    
        