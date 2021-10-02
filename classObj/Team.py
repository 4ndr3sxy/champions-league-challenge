"""Class/ object Team"""


class Team:
    """Constructor"""
    def __init__(self, name=0, league="", iq=0):
        self.__name = name
        self.__league = league
        self.__iq = iq

    """Get name"""
    def get_name(self):
        return self.__name

    """Set name"""
    def set_name(self, value):
        self.__name = value

    """Get league of the team"""
    def get_league(self):
        return self.__league

    """Set leagie to team"""
    def set_league(self, value):
        self.__league == value

    """Get league of the team"""
    def get_iq(self):
        return self.__iq

    """Set leagie to team"""
    def set_iq(self, value):
        self.__iq = value

    name = property(get_name, set_name)
    league = property(get_league, set_league)
    iq = property(get_iq, set_iq)
