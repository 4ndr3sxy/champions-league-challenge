"""Class/ object Pot"""


class Pot:

    """Constructor"""
    def __init__(self, name=0, team=None):
        self.__name = name
        self.__teams = []
        self.__teams.append(team)

    """Get name"""
    def get_name(self):
        return self.__name

    """Set name"""
    def set_name(self, value):
        self.__name = value

    """Get list_team"""
    def get_teams(self):
        return self.__teams

    """Set team to list_team"""
    def set_teams(self, value):
        self.__teams.append(value)

    name = property(get_name, set_name)
    teams = property(get_teams, set_teams)

    def create_pots(cup):
        """Code here"""
