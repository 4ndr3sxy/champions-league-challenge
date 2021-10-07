from classObj.Cup import Cup
from classObj.Pot import Pot
from classObj.Team import Team
from classObj.Data_burn import Data


print("----------------------")
print("TEST NO objects concat")
print("----------------------")


list_teams = []

obj_data = Data
obj_data.create_list_object_team()

"""Test Cup Eufa"""
print("Test Cup object 1")
obj1 = Cup("Eufa", 32)
print(obj1.name)
print(obj1.count_teams)
print("----------")
obj1.name = "EUFA"
obj1.count_teams = 16
print(obj1.name)
print(obj1.count_teams)

"""Test Cup League"""
print("\nTest Cup object 2")
obj2 = Cup("Inglesa", 16)
print(obj2.name)
print(obj2.count_teams)
obj2.name = "INGLESA"
print("----------")
obj2.count_teams = 8
print(obj2.name)
print(obj2.count_teams)

"""Test Team"""
print("\nTest Team object")
obj3 = Team("PSG", obj2, 80)
print(obj3.name)
print(obj3.league.name)
print(obj3.league.count_teams)
print(obj3.iq)
print("----------")
obj3.name = "psg"
obj3.league = "algo"#check this/understand
obj3.iq = 40
print(obj3.name)
print(obj3.league.name)
print(obj3.league.count_teams)
print(obj3.iq)

print("\nTest Team object 2")
obj31 = Team("ARSENAL", obj2, 99)
print(obj31.name)
print(obj31.league.name)
print(obj31.league.count_teams)
print(obj31.iq)
print("----------")
obj31.name = "Arsenal"
obj31.league = "algo"#check this/understand
obj31.iq = 57
print(obj31.name)
print(obj31.league.name)
print(obj31.league.count_teams)
print(obj31.iq)

"""Test Pot object"""
print("\nTest Pot object")
obj4 = Pot(1, obj3)
obj4.teams = obj31
print(obj4.name)
for i in obj4.teams:
    print("\t" + i.name)
    print("\t" + i.league.name)
    print("\t" + str(i.league.count_teams))
    print("\t" + str(i.iq))
    print("\t----")
print("----------")
