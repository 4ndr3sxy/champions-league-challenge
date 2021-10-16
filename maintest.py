from classObj.Cup import Cup
from classObj.Pot import Pot
from classObj.Team import Team
from classObj.Data_burn import Data
import random


print("----------------------")
print("TEST NO objects concat")
print("----------------------")


list_teams = []

obj_data = Data
print("$$$$$")
obj_data.create_list_object_team()
print("$$$$$")

"""Test Cup Eufa"""
print("Test Cup object 1")
obj1 = Cup("Eufa")
print(obj1.name)
print("----------")
obj1.name = "EUFA"
print(obj1.name)

"""Test Cup League"""
print("\nTest Cup object 2")
obj2 = Cup("Inglesa")
print(obj2.name)
obj2.name = "INGLESA"
print("----------")
print(obj2.name)

"""Test Team"""
print("\nTest Team object")
obj3 = Team("PSG", obj2, 80)
print(obj3.name)
print(obj3.league.name)
print(obj3.iq)
print("----------")
obj3.name = "psg"
obj3.league = "algo"  # check this/understand
obj3.iq = 40
print(obj3.name)
print(obj3.league.name)
print(obj3.iq)

print("\nTest Team object 2")
obj31 = Team("ARSENAL", obj2, 99)
print(obj31.name)
print(obj31.league.name)
print(obj31.iq)
print("----------")
obj31.name = "Arsenal"
obj31.league = "algo"  # check this/understand
obj31.iq = 57
print(obj31.name)
print(obj31.league.name)
print(obj31.iq)

"""Test Pot object"""
print("\nTest Pot object")
obj4 = Pot(1, obj3)
obj4.teams = obj31
print(obj4.name)
for i in obj4.teams:
    print("\t" + i.name)
    print("\t" + i.league.name)

    print("\t" + str(i.iq))
    print("\t----")
print("----------")

print("\n\nLast one test")

cups = [[]]
count_teams = 0
name_cups = []
name_teams = []
"""Import list of objects"""
list_objects = Data.teams_list
"""Create team and Cups"""
validate_name_Cup = False
for team, league in list_objects:
    if league not in name_cups:
        name_cups.append(league)
        new_league = Cup(league)
        cups.append(new_league)
    else:
        for cup in cups:
            if type(cup) is Cup and cup.name == league:
                new_league = cup
                break
    iq_random = random.randint(1, 100)
    new_team = Team(team, new_league, iq_random)
    new_league.teams = new_team
    # print(new_league)

print("----")
print(cups)
print("----")

for cup in cups:
    print("----")
    if type(cup) is Cup:
        print("Cup:")
        print(cup)
        print("\nTeams:")
        cup.show_teams()
        print("\nTeams Objects")
        print(cup.teams)
    print("----")
