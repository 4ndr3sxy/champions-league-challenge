"""Class/ object Cup"""


class Cup:
    __count_teams = 0
    """Constructor"""
    def __init__(self, name=""):
        self.__name = name
        self.__teams = []

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
        self.__teams.append(value)
        self.__count_teams += 1

    name = property(get_name, set_name)
    teams = property(get_teams, set_teams)

    def create_groups(list=[]):
        """Code here"""

    def compare_teams(pot, new_team):
        """Code here"""

    def next_round(list=[]):
        """Code here"""

    def show_teams(self):
        for team in self.teams:
            print(team)

    def __str__(self):
        information = ""
        information += self.name + " - "
        information += str(self.__count_teams)
        return information
