"""Class/ object Cup"""

import random
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

    def create_groups(self, list=[[]], count=8):
        self.__groups = []
        for i in range(0, count):
            group = Group()
            self.__groups.append(group)
        for pot in list:
            index = 0
            for teams in pot:
                self.__groups[index].teams = teams
                index += 1
        return self.__groups

    def compare_teams(self, team, new_team):
        if team.league.name == new_team.league.name:
            return False
        return True

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

    def clean_result(self):
        print("entro")
        for team in self.__teams:
            # print("1---")
            # print(team.points)
            team.points = 0
            # team.__wins = 0
            # team.__lose = 0
            # team.__tie = 0
            # print(team.points)
            # print("2---")

    def shuffle(self, pot_head, pot_n_head):        
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
        octavos = []
        j = 0
        while j < len(pot_head.teams):
            flag = False
        # for j in range(0, len(pot_head.teams)):
            # print("INIT")
            rnd = 0
            vs = []
            rnd = random.randint(0, 7)
            size = len(octavos)
            for i in range(0,size):
                # print("Init i")
                if pot_n_head.teams[rnd] in octavos[i][1:]:
                    # print("if RND")
                    # print("--{}--".format(j))
                    # print("{} ---- {}".format(octavos, rnd))
                    flag = True
                    break
            # print("if flag")
            if flag is False:
                # print("if compare teams")
                if self.compare_teams(pot_head.teams[j], pot_n_head.teams[rnd]):
                    # print("added in array")
                    vs.append(pot_head.teams[j])    
                    vs.append(pot_n_head.teams[rnd])
                    octavos.append(vs)
                    j += 1

        return octavos

            # if rnd in octavos
            # print(rnd)     
