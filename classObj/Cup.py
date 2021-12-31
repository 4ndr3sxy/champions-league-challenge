"""Class/ object Cup"""


from typing import List
from classObj.Group import Group


class Cup:
    __count_teams = 0
    """Constructor"""
    def __init__(self, name=""):
        self.__name = name
        self.__teams = []
        self.__groups = []

    """Get name"""
    def get_name(self):
        return self.__name

    """Set name"""
    def set_name(self, value):
        self.__name = value

    """Get teams"""
    def get_teams(self):
        return self.__teams

    """Set team to teams"""
    def set_teams(self, value):
        if type(value) is list:
            for team in value:
                self.__teams.append(team)
                self.__count_teams += 1
        else:
            self.__teams.append(value)
            self.__count_teams += 1

    name = property(get_name, set_name)
    teams = property(get_teams, set_teams)

    def create_groups(self, list=[[]]):
        for i in range(0, 8):
            group = Group()
            self.__groups.append(group)
        for pot in list:
            index = 0
            for teams in pot:
                self.__groups[index].teams = teams
                index += 1
        return self.__groups

    def compare_teams(self, pot, new_team):
        """Code here"""

    def next_round(self, list=[]):
        """Code here"""

    def show_teams(self):
        for team in self.teams:
            if team is not None:
                print(team)

    def __str__(self):
        information = ""
        information += self.name + " - "
        information += str(self.__count_teams)
        return information

    def clean_teams(self):
        self.__teams = []
        self.__count_teams = 0

    def shuffle(self, pot_1, pot_2):
        pass
        """
        Logic to select random vs between teams head and NO head
        1)random to get position in index 
        2) validate if the team in this position is another league
        3)YES: save
        4)NO: again step 1
        5)Return: array bidimentional, example: [[0,5], [1,3], [8, 6]]
            [0, 5]-> first position(0) is position of team in POT head
            [0, 5]-> second position(5) is position of team in POT no head
        """
