"""Class/ object Pot"""


class Pot:

    """Constructor"""
    def __init__(self, name=0, count=0):
        self.__name = name
        self.__teams = []
        self.__count_teams = count
        # self.__teams.append(team)

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

    def create_pot(self, cup):
        count = 0
        for team in cup:
            if count >= self.__count_teams:
                if team not in self.__teams:
                    self.__teams.append(team)
                    self.__count_teams += 1
                    if self.__count_teams % 8 == 0:
                        break
            count += 1
        # print("&&&&&")
        # for team in self.__teams:
        #     print(team)
        # print("&&&&&")
        return self.__teams

    def clean(self):
        self.__teams = []

    name = property(get_name, set_name)
    teams = property(get_teams, set_teams)
