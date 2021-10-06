"""Class/ object Cup"""


from _typeshed import Self


class Cup:
    """Constructor"""
    def __init__(self, name="", count_teams=0):
        self.__name = name
        self.__count_teams = count_teams
        self.__teams = None

    """Get name"""
    def get_name(self):
        return self.__name

    """Set name"""
    def set_name(self, value):
        self.__name = value

    """Get count_teams"""
    def get_count_teams(self):
        return self.__count_teams

    """Set count_teams"""
    def set_count_teams(self, value):
        self.__count_teams = value

    """Get teams"""
    def get_teams(self):
        return self.__teams

    """Set team to teams"""
    def set_teams(self, value):
        self.__teams.append(value)

    name = property(get_name, set_name)
    count_teams = property(get_count_teams, set_count_teams)
    teams = property(get_teams, set_teams)

    def create_groups(list=[]):
        """Code here"""

    def compare_teams(pot, new_team):
        """Code here"""

    def next_round(list=[]):
        """Code here"""
